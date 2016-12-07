package main

import (
	"fmt"
	"io/ioutil"
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

func main() {
	data := load_data("day2.data")

	// Start in the middle
	curr_x, curr_y := 1, 1
	keypad := [3][3]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9}}

	for i := 0; i < len(data); i++ {
		//fmt.Printf("(%d,%d): %d\n", curr_x, curr_y, keypad[curr_y][curr_x])

		for _, r := range data[i] {
			switch r {
			case 'U':
				curr_y -= 1
				if curr_y < 0 {
					curr_y = 0
				}
			case 'D':
				curr_y += 1
				if curr_y > 2 {
					curr_y = 2
				}
			case 'L':
				curr_x -= 1
				if curr_x < 0 {
					curr_x = 0
				}
			case 'R':
				curr_x += 1
				if curr_x > 2 {
					curr_x = 2
				}
			}
			//fmt.Printf("(%d,%d): %d\n", curr_x, curr_y, keypad[curr_y][curr_x])
		}
		fmt.Printf("Instruction %d: %d\n", i, keypad[curr_y][curr_x])
	}
}
