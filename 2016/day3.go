package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"sort"
	"strconv"
	"strings"
)

func canMakeTriangle(lst []int) bool {
	sort.Ints(lst)
	return lst[0]+lst[1] > lst[2]
}

func showUsage() {
	fmt.Printf("Usage: %s [1|2]\n", os.Args[0])
	os.Exit(1)
}

func readData(filename string) ([][]int, error) {
	b, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Print(err)
		return nil, err
	}

	input_str := string(b)
	input_lines := strings.Split(input_str, "\n")
	input_count := len(input_lines)
	int_lists := make([][]int, input_count)

	for i := 0; i < len(input_lines); i++ {
		nums := strings.Fields(input_lines[i])
		if len(nums) == 0 {
			input_count -= 1
			continue
		}
		int_lists[i] = make([]int, len(nums))

		for j := 0; j < len(nums); j++ {
			int_lists[i][j], err = strconv.Atoi(nums[j])
			if err != nil {
				return nil, err
			}
		}

	}
	return int_lists[:input_count], nil
}

func main() {
	data, err := readData("day3.data")
	if err != nil {
		fmt.Printf("%s", err)
		return
	}
	acc := 0

	if len(os.Args) != 2 {
		showUsage()
	} else if strings.Compare(os.Args[1], "1") == 0 {
		for i := 0; i < len(data); i++ {
			if canMakeTriangle(data[i]) {
				acc += 1
			}
		}
	} else if strings.Compare(os.Args[1], "2") == 0 {
		tmp := make([]int, 3)
		// Process groups of 3
		for i := 0; i < len(data); i += 3 {
			for j := 0; j < 3; j++ {
				for k := 0; k < 3; k++ {
					tmp[k] = data[i+k][j]
				}
				if canMakeTriangle(tmp) {
					acc += 1
				}
			}
		}
	} else {
		showUsage()
	}

	fmt.Printf("Number of triangles that could be made: %d\n", acc)
}
