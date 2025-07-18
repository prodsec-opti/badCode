using System;
using System.IO;
using System.Web;
using System.Web.UI;
using System.Data.SqlClient;
using System.Diagnostics;
using System.Text;
using System.Xml;
using System.Runtime.Serialization.Formatters.Binary;
using System.IdentityModel.Tokens.Jwt;

namespace VulnerableWebApp
{
    public partial class Default : Page
    {
        // 🚨 Hardcoded secrets
        private const string JWT_SECRET = "hardcodedSecretKeyForJWT123!";
        private const string DB_PASSWORD = "SuperSecretP@ssword";

        protected void Page_Load(object sender, EventArgs e)
        {
            // 🚨 Reflected XSS
            string q = Request.QueryString["q"];
            Response.Write("<html><body>Search results for: " + q + "</body></html>");

            // 🚨 SQL Injection
            string user = Request.QueryString["user"];
            string pass = Request.QueryString["pass"];
            using (SqlConnection conn = new SqlConnection("Server=localhost;Database=TestApp;User Id=sa;Password=" + DB_PASSWORD + ";"))
            {
                conn.Open();
                string sql = "SELECT * FROM users WHERE username = '" + user + "' AND password = '" + pass + "'";
                SqlCommand cmd = new SqlCommand(sql, conn);
                SqlDataReader reader = cmd.ExecuteReader();
                while (reader.Read())
                {
                    Response.Write("Welcome, " + reader["fullname"] + "<br>");
                }
            }

            // 🚨 Command Injection
            string cmdInput = Request.QueryString["cmd"];
            if (!string.IsNullOrEmpty(cmdInput))
            {
                Process.Start("cmd.exe", "/C " + cmdInput);
            }

            // 🚨 Insecure JWT decoding (no validation)
            string token = Request.QueryString["token"];
            if (!string.IsNullOrEmpty(token))
            {
                var handler = new JwtSecurityTokenHandler();
                var jwt = handler.ReadJwtToken(token);
                Response.Write("JWT payload: " + jwt.Subject);
            }
        }

        protected void UploadButton_Click(object sender, EventArgs e)
        {
            // 🚨 Insecure file upload
            HttpPostedFile file = Request.Files["upload"];
            string savePath = Server.MapPath("~/uploads/") + Path.GetFileName(file.FileName);
            file.SaveAs(savePath);
            Response.Write("File uploaded to: " + savePath);
        }

        protected void ParseXML_Click(object sender, EventArgs e)
        {
            // 🚨 XXE vulnerability
            string xmlData = Request.Form["xml"];
            XmlDocument doc = new XmlDocument();
            doc.XmlResolver = new XmlUrlResolver(); // insecure
            doc.LoadXml(xmlData);
            Response.Write("Root element: " + doc.DocumentElement.Name);
        }

        protected void Deserialize_Click(object sender, EventArgs e)
        {
            // 🚨 Insecure deserialization
            string base64 = Request.Form["payload"];
            byte[] bytes = Convert.FromBase64String(base64);
            BinaryFormatter formatter = new BinaryFormatter();
            using (MemoryStream ms = new MemoryStream(bytes))
            {
                object obj = formatter.Deserialize(ms);
                Response.Write("Deserialized object: " + obj.ToString());
            }
        }
    }
}
