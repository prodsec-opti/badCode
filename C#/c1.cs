using System;
using System.Data.SqlClient;
using System.Diagnostics;
using System.Runtime.Serialization.Formatters.Binary;
using System.IO;

namespace VulnerableApp
{
    class Program
    {
        // Vulnerability 1: SQL Injection (CWE-89)
        static void GetUser(string username)
        {
            string connectionString = "Server=localhost;Database=test;User ID=sa;Password=;";
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                string query = "SELECT * FROM Users WHERE Username = '" + username + "'"; // SQLi
                SqlCommand command = new SqlCommand(query, connection);
                connection.Open();
                SqlDataReader reader = command.ExecuteReader();
                while (reader.Read())
                {
                    Console.WriteLine(reader["Username"]);
                }
            }
        }

        // Vulnerability 2: Command Injection (CWE-78)
        static void PingHost(string host)
        {
            Process.Start("cmd.exe", "/C ping " + host); // Command injection
        }

        // Vulnerability 3: Insecure Deserialization (CWE-502)
        static object DeserializeData(byte[] data)
        {
            BinaryFormatter formatter = new BinaryFormatter();
            using (MemoryStream ms = new MemoryStream(data))
            {
                return formatter.Deserialize(ms); // Insecure deserialization
            }
        }

        // Vulnerability 4: Hardcoded Cryptographic Key (CWE-321)
        static string EncryptData(string data)
        {
            string encryptionKey = "thisisabadkey123"; // Hardcoded crypto key
            // ... encryption logic ...
            return "encrypted_data";
        }

        // Vulnerability 5: Exposed Secrets
        const string AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE";
        const string AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY";
        const string DB_PASSWORD = "SuperSecretDBPassword123!";

        static void Main(string[] args)
        {
            if (args.Length > 0)
            {
                GetUser(args[0]);
                PingHost(args[0]);
            }

            Console.WriteLine("Application running with insecure configurations!");
        }
    }
}