package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
)

func main() {
    fmt.Println("Hello, World!")
}

func readFile(){
    file, err := os.Open("C:\\Users\\jonat\\Documents\\GitHub\\AdventOfCode2023\\day2\\input.txt")
    if err != nil{
        log.Fatal(err)
    }
    defer file.Close()

    scanner:= bufio.NewScanner(file)

    for scanner.Scan(){
        fmt.Println(scanner.Text())
    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }
}