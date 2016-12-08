package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func load_data(filename string) []string {
	b, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Print(err)
	}
	input_str := string(b)
	return strings.Split(input_str, "\n")
}

func showUsage() {
	fmt.Printf("Usage: %s [1|2]\n", os.Args[0])
	os.Exit(1)
}

func main() {
	data := load_data("day2.data")


	// Start in the middle
	keypad1 := [][]string{
		{"0", "0", "0", "0", "0"},
		{"0", "1", "2", "3", "0"},
		{"0", "4", "5", "6", "0"},
		{"0", "7", "8", "9", "0"},
		{"0", "0", "0", "0", "0"}}

	keypad2 := [][]string{
		{"0", "0", "0", "0", "0", "0", "0"},
		{"0", "0", "0", "1", "0", "0", "0"},
		{"0", "0", "2", "3", "4", "0", "0"},
		{"0", "5", "6", "7", "8", "9", "0"},
		{"0", "0", "A", "B", "C", "0", "0"},
		{"0", "0", "0", "D", "0", "0", "0"},
		{"0", "0", "0", "0", "0", "0", "0"}}

	var keypad [][]string
	var curr_x, curr_y int
	if (len(os.Args) != 2) {
		showUsage()
	} else if (strings.Compare(os.Args[1], "1") == 0) {
		keypad = keypad1
		curr_x, curr_y = 2,2
	} else if (strings.Compare(os.Args[1], "2") == 0) {
		keypad = keypad2
		curr_x, curr_y = 1,3
	} else {
		showUsage()
	}
	//curr_x, curr_y := len(keypad)/2, len(keypad)/2
	
	fmt.Printf("Starting at (%d,%d)\n", curr_x, curr_y)
	for i := 0; i < len(data); i++ {
		//fmt.Printf("(%d,%d): %s\n", curr_x, curr_y, keypad[curr_y][curr_x])

		for _, r := range data[i] {
			switch r {
			case 'U':
				curr_y -= 1
				if strings.Compare(keypad[curr_y][curr_x], "0") == 0 {
					curr_y += 1
				}
			case 'D':
				curr_y += 1
				if strings.Compare(keypad[curr_y][curr_x], "0") == 0 {
					curr_y -= 1
				}
			case 'L':
				curr_x -= 1
				if strings.Compare(keypad[curr_y][curr_x], "0") == 0 {
					curr_x += 1
				}
			case 'R':
				curr_x += 1
				if strings.Compare(keypad[curr_y][curr_x], "0") == 0 {
					curr_x -= 1
				}
			}
			//fmt.Printf("(%d,%d): %s\n", curr_x, curr_y, keypad[curr_y][curr_x])
		}
		fmt.Printf("Instruction %d: %s\n", i, keypad[curr_y][curr_x])
	}
}
