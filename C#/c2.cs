// using System;
// using System.Web;
// using System.Web.UI;
// using System.IO;
// using System.Xml;
// using System.Xml.Serialization;
// using System.Diagnostics;
// using System.IdentityModel.Tokens.Jwt;
// using System.Text;

// namespace VulnerableWebApp
// {
//     public partial class Default : Page
//     {
//         // 🚨  secrets
//         private const string jwtSecret = "supersecretkeythatshouldnotbeinhere123!";
//         private const string dbPassword = "P@ssw0rd123!";

//         protected void Page_Load(object sender, EventArgs e)
//         {
//             // 🚨 Reflected 
//             string searchQuery = Request.QueryString["q"];
//             Response.Write("Search results for: " + searchQuery);

//             // 🚨  deserialization
//             string serializedObject = Request.Form["payload"];
//             if (!string.IsNullOrEmpty(serializedObject))
//             {
//                 XmlSerializer serializer = new XmlSerializer(typeof(User));
//                 using (TextReader reader = new StringReader(serializedObject))
//                 {
//                     var obj = (User)serializer.Deserialize(reader);
//                     Response.Write("Deserialized user: " + obj.Username);
//                 }
//             }

//             // 🚨 Command 
//             string userInput = Request.QueryString["cmd"];
//             if (!string.IsNullOrEmpty(userInput))
//             {
//                 Process.Start("cmd.exe", "/C " + userInput);
//             }

//             // 🚨 Insecure JWT 
//             string token = Request.QueryString["token"];
//             if (!string.IsNullOrEmpty(token))
//             {
//                 var handler = new JwtSecurityTokenHandler();
//                 var jwtToken = handler.ReadJwtToken(token);
//                 Response.Write("JWT Subject: " + jwtToken.Subject);
//             }
//         }

//         // 🚨 File upload 
//         protected void Upload_Click(object sender, EventArgs e)
//         {
//             HttpPostedFile file = Request.Files["upload"];
//             string savePath = Server.MapPath("~/uploads/") + Path.GetFileName(file.FileName);
//             file.SaveAs(savePath);
//             Response.Write("File uploaded to: " + savePath);
//         }

//         // 🚨 XML External Entity (XXE)
//         protected void ParseXML_Click(object sender, EventArgs e)
//         {
//             string xmlData = Request.Form["xmlInput"];
//             XmlDocument doc = new XmlDocument();
//             doc.XmlResolver = new XmlUrlResolver(); // insecure
//             doc.LoadXml(xmlData);
//             Response.Write("Root element: " + doc.DocumentElement.Name);
//         }
//     }

//     public class User
//     {
//         public string Username { get; set; }
//     }
// }
