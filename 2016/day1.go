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

/* Takes the current (x,y) position, the direction to go, and the number of steps
 * Returns the new (x,y) position. As well as strings representing every step taken
 */
func do_steps(curr_x int, curr_y int, dir int, steps int) (int, int, []string) {
	ret_steps := make([]string, steps)

	for i := 0; i < steps; i++ {
		switch dir {
		case UP:
			curr_x += 1
		case DOWN:
			curr_x -= 1
		case RIGHT:
			curr_y += 1
		case LEFT:
			curr_y -= 1
		}
		ret_steps[i] = fmt.Sprintf("%d,%d", curr_x, curr_y)
	}

	return curr_x, curr_y, ret_steps
}

func main() {
	var input_file string = "day1.data"
	data := read_data(input_file)

	curr_dir := UP
	curr_x, curr_y := 0, 0
	all_steps := make(map[string]int)

	var step_list []string

	for _, element := range data {
		turn_dir, turn_steps := parse_direction(element)
		curr_dir = apply_turn(curr_dir, turn_dir)

		curr_x, curr_y, step_list = do_steps(curr_x, curr_y, curr_dir, turn_steps)
		/* This section can be commented out to get the answer to part 1 */
		for i := 0; i < len(step_list); i++ {
			if _, found := all_steps[step_list[i]]; found {
				fmt.Printf("Crossed a previous path at (%s)\n", step_list[i])
				return
			} else {
				all_steps[step_list[i]] = 1
			}
		}
	}
	fmt.Printf("current position (%d, %d)\n", curr_x, curr_y)
}
