package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

const (
	UP       = iota
	RIGHT    = iota
	DOWN     = iota
	LEFT     = iota
	NUM_DIRS = 4
)

func apply_turn(curr_dir int, turn_dir string) int {
	if turn_dir == "L" {
		curr_dir -= 1
	} else if turn_dir == "R" {
		curr_dir += 1
	} else {
		fmt.Printf("Unknown direction encountered '%s'. Doing nothing...", turn_dir)
	}
	// Funny return to deal with "negative" directions nicely
	return (curr_dir + NUM_DIRS) % NUM_DIRS
}

func read_data(filename string) []string {
	b, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Print(err)
	}
	input_str := string(b)
	s := strings.Split(input_str, ",")

	return s
}

func parse_direction(dir string) (string, int) {
	trimmed_dir := strings.TrimSpace(dir)
	turn_dir := string(trimmed_dir[0])
	turn_steps, err := strconv.Atoi(trimmed_dir[1:])
	if err != nil {
		fmt.Printf("Unable to convert '%s' to an integer. Exiting...", trimmed_dir[1:])
		os.Exit(-1)
	}

	return turn_dir, turn_steps
}

func main() {
	var input_file string = "day1.data"
	data := read_data(input_file)

	curr_dir := UP
	curr_x, curr_y := 0, 0

	for _, element := range data {
		turn_dir, turn_steps := parse_direction(element)
		curr_dir = apply_turn(curr_dir, turn_dir)

		switch curr_dir {
		case UP:
			curr_x += turn_steps
		case DOWN:
			curr_x -= turn_steps
		case RIGHT:
			curr_y += turn_steps
		case LEFT:
			curr_y -= turn_steps
		}

		fmt.Printf("Heading '%d' and taking '%d' steps\n", curr_dir, turn_steps)
		fmt.Printf("current position (%d, %d)\n", curr_x, curr_y)
	}
}
