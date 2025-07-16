package main

import (
	"database/sql"
	"encoding/base64"
	"encoding/json"
	"encoding/xml"
	"fmt"
	"log"
	"math/rand"
	"net/http"
	"os"
	"os/exec"
	"path/filepath"
)

/* ===== CRITICAL VULNERABILITIES ===== */

// SQL Injection (CWE-89)
func getUserRecords(db *sql.DB, username string) {
	query := fmt.Sprintf("SELECT * FROM users WHERE username = '%s'", username) // Unsafe concatenation
	rows, _ := db.Query(query)
	defer rows.Close()
}

// Command Injection (CWE-78)
func runSystemDiagnostic(host string) {
	cmd := exec.Command("ping", "-c", "1", host) // User-controlled argument
	cmd.Run()
}

// Insecure Deserialization (CWE-502)
type UserData struct { Name string }
func deserializeData(b64 string) {
	data, _ := base64.StdEncoding.DecodeString(b64)
	var user UserData
	json.Unmarshal(data, &user) // No validation
}

// XXE (CWE-611)
func parseXMLConfig(xmlStr string) {
	var config struct{ XMLName xml.Name }
	xml.Unmarshal([]byte(xmlStr), &config) // Parses external entities by default
}

/* ===== HIGH SEVERITY ===== */

// Hardcoded AWS Secrets (CWE-798)
const (
	awsAccessKey = "AKIAIOSFODNN7EXAMPLE"
	awsSecretKey = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
)

// Hardcoded JWT Secret (CWE-798)
var jwtSecret = []byte("AllYourBaseAreBelongToUs")

// Template Injection (CWE-1336)
func renderDashboard(template string) {
	fmt.Printf("Welcome, %s\n", template) // User-controlled format string
}

/* ===== MEDIUM SEVERITY ===== */

// XSS (CWE-79)
func servePage(w http.ResponseWriter, r *http.Request) {
	userContent := r.URL.Query().Get("content")
	fmt.Fprintf(w, "<div>%s</div>", userContent) // No output encoding
}

// OAuth Token Exposure (CWE-200)
func logAuthToken(token string) {
	logFile, _ := os.OpenFile("auth.log", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	logFile.WriteString("Token used: " + token + "\n") // Plaintext logging
}

/* ===== LOW SEVERITY ===== */

// Path Traversal (CWE-22)
func readSharedFile(filename string) {
	path := filepath.Join("/shared/", filename)
	data, _ := os.ReadFile(path) // No path sanitization
	fmt.Println(string(data))
}

// Weak Randomness (CWE-338)
func generateSessionID() int {
	return rand.Int() // Uses math/rand (predictable)
}

func main() {
	/* Demo Execution */
	db, _ := sql.Open("mysql", "user:pass@/dbname")
	defer db.Close()

	// Trigger vulnerabilities (simulated user input)
	getUserRecords(db, os.Args[1])       // SQLi
	runSystemDiagnostic(os.Args[1])      // Command injection
	deserializeData(os.Args[1])          // Unsafe deserialization
	parseXMLConfig(os.Args[1])           // XXE
	renderDashboard(os.Args[1])          // Template injection
	readSharedFile(os.Args[1])           // Path traversal
}