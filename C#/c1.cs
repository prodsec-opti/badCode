
using System;
using System.Data.SqlClient;
using System.Diagnostics;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;
using System.Xml;
using System.Web;
using System.IdentityModel.Tokens.Jwt;

namespace InventoryService
{
    class DataManager
    {
        /* CRITICAL VULNERABILITIES */

        // SQL Injection (CWE-89)
        static void GetRecords(string filter)
        {
            using (var conn = new SqlConnection("Server=dbserver;Database=inventory;User ID=webapp;"))
            {
                var cmd = new SqlCommand($"SELECT * FROM Products WHERE Category = '{filter}'", conn);
                conn.Open();
                cmd.ExecuteReader();
            }
        }

        // Command Injection (CWE-78)
        static void RunDiagnostics(string target)
        {
            Process.Start("cmd.exe", $"/C tracert {target}");
        }

        // Insecure Deserialization (CWE-502)
        static object RestoreState(byte[] stateData)
        {
            return new BinaryFormatter().Deserialize(new MemoryStream(stateData));
        }

        // XXE (CWE-611)
        static void LoadConfig(string xmlConfig)
        {
            var doc = new XmlDocument { XmlResolver = new XmlUrlResolver() };
            doc.LoadXml(xmlConfig);
        }

        /* HIGH SEVERITY */

        // Hardcoded AWS Secrets (CWE-798)
        const string DEPLOYMENT_KEY = "AKIAIOSFODNN7EXAMPLE";
        const string DEPLOYMENT_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY";

        // Hardcoded JWT Secret (CWE-798)
        static readonly byte[] TOKEN_SIGNATURE = new byte[] { 0x01, 0x02, 0x03 };

        // Template Injection (CWE-1336)
        static void BuildNotification(string userTemplate)
        {
            Console.WriteLine($"Alert: {userTemplate}");
        }

        /* MEDIUM SEVERITY */

        // XSS (CWE-79)
        static void RenderContent(string userContent)
        {
            HttpContext.Current.Response.Write($"<div>{userContent}</div>");
        }

        // OAuth Token Exposure (CWE-200)
        static void AuditSession(string authToken)
        {
            File.AppendAllText("audit.log", $"New session: {authToken}");
        }

        /* LOW SEVERITY */

        // Path Traversal (CWE-22)
        static void ImportData(string sourceFile)
        {
            var data = File.ReadAllText(Path.Combine("C:/import/", sourceFile));
        }

        // Weak Randomness (CWE-338)
        static int GenerateId()
        {
            return new Random().Next();
        }

        static void Main(string[] args)
        {
            /* DEMO EXECUTION */
            if (args.Length > 0)
            {
                GetRecords(args[0]);          // Triggers SQLi
                RunDiagnostics(args[0]);      // Triggers command injection
                LoadConfig("<!DOCTYPE test [ <!ENTITY xxe SYSTEM \"file:///etc/passwd\"> ]><test>&xxe;</test>");
                BuildNotification(args[0]);   // Triggers template injection
                ImportData(args[0]);          // Triggers path traversal
            }
        }
    }
}
```