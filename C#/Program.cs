using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.FileProviders;
using System.Diagnostics;
using System.Security.Claims;
using System.Text;
using System.Text.Json;
using System.Xml;
using System.IO.Compression;
using System.Runtime.Serialization.Formatters.Binary;
using Microsoft.IdentityModel.Tokens;
using System.IdentityModel.Tokens.Jwt;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// 🚨 Hardcoded secrets
string JWT_SECRET = "superSecretJWTKey123456!";
string DB_PASSWORD = "P@ssw0rd123!";

// 🚨 Reflected XSS
app.MapGet("/search", (HttpRequest req) =>
{
    var query = req.Query["q"];
    return Results.Content($"<html><body>Search results for: {query}</body></html>", "text/html");
});

// 🚨 Command Injection
app.MapGet("/exec", async (HttpRequest req) =>
{
    string cmd = req.Query["cmd"];
    if (!string.IsNullOrWhiteSpace(cmd))
    {
        var proc = Process.Start("cmd.exe", "/C " + cmd);
        proc.WaitForExit();
        return Results.Text("Executed: " + cmd);
    }
    return Results.BadRequest("No command provided.");
});

// 🚨 Insecure JWT (no validation)
app.MapGet("/jwt", (HttpRequest req) =>
{
    var token = req.Query["token"];
    var handler = new JwtSecurityTokenHandler();
    var jwt = handler.ReadJwtToken(token);
    return Results.Text("JWT Subject: " + jwt.Subject);
});

// 🚨 File upload without validation
app.MapPost("/upload", async (HttpRequest req) =>
{
    var form = await req.ReadFormAsync();
    var file = form.Files.GetFile("file");
    var path = Path.Combine("uploads", file.FileName);
    Directory.CreateDirectory("uploads");
    using var stream = new FileStream(path, FileMode.Create);
    await file.CopyToAsync(stream);
    return Results.Text("File saved at: " + path);
});

// 🚨 XXE (XML External Entity)
app.MapPost("/xxe", async (HttpRequest req) =>
{
    var xmlString = await new StreamReader(req.Body).ReadToEndAsync();
    var xmlDoc = new XmlDocument
    {
        XmlResolver = new XmlUrlResolver() // ⚠️ Insecure
    };
    xmlDoc.LoadXml(xmlString);
    return Results.Text("Root element: " + xmlDoc.DocumentElement.Name);
});

// 🚨 Insecure deserialization
app.MapPost("/deserialize", async (HttpRequest req) =>
{
    var base64 = await new StreamReader(req.Body).ReadToEndAsync();
    var bytes = Convert.FromBase64String(base64);
    var formatter = new BinaryFormatter();
#pragma warning disable SYSLIB0011
    using var ms = new MemoryStream(bytes);
    var obj = formatter.Deserialize(ms);
#pragma warning restore SYSLIB0011
    return Results.Text("Deserialized: " + obj.ToString());
});

app.Run();
