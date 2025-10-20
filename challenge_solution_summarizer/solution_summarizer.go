package main

import (
	"bufio"
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"
)

func main() {
	fmt.Println("Pega el texto y presiona ENTER dos veces para resumir:")

	reader := bufio.NewReader(os.Stdin)
	var input strings.Builder

	for {
		line, err := reader.ReadString('\n')
		if err != nil && len(line) == 0 {
			fmt.Fprintln(os.Stderr, "error leyendo entrada:", err)
			return
		}
		line = strings.TrimSpace(line)
		if line == "" {
			break
		}
		input.WriteString(line + " ")
	}

	body := map[string]string{"text": input.String()}
	jsonData, err := json.Marshal(body)
	if err != nil {
		fmt.Fprintln(os.Stderr, "error preparando JSON:", err)
		return
	}

	resp, err := http.Post("http://localhost:5678/webhook-test/resumen", "application/json", bytes.NewBuffer(jsonData))
	if err != nil {
		fmt.Fprintln(os.Stderr, "error al solicitar resumen:", err)
		return
	}
	defer resp.Body.Close()

	result, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Fprintln(os.Stderr, "error leyendo respuesta:", err)
		return
	}
	fmt.Println("\nResumen:\n", string(result))
}
