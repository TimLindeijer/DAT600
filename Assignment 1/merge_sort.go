package main

import (
	"fmt"
	"math/rand"
	"time"
)

var inputSizes = []int{10, 100, 1000, 10000}

func merge(arr []int, left []int, right []int) int {
	steps := 0
	i, j, k := 0, 0, 0

	for i < len(left) && j < len(right) {
		if left[i] < right[j] {
			arr[k] = left[i]
			i++
		} else {
			arr[k] = right[j]
			j++
		}
		k++
		steps++
	}

	for i < len(left) {
		arr[k] = left[i]
		i++
		k++
		steps++
	}

	for j < len(right) {
		arr[k] = right[j]
		j++
		k++
		steps++
	}

	return steps
}

func mergeSort(arr []int) int {
	steps := 0
	if len(arr) > 1 {
		mid := len(arr) / 2
		left := arr[:mid]
		right := arr[mid:]

		steps += mergeSort(left)
		steps += mergeSort(right)

		steps += merge(arr, left, right)
	}

	return steps
}

func main() {
	for _, size := range inputSizes {
		arr := rand.Perm(size) // Generate a random permutation of size
		startTime := time.Now()

		steps := mergeSort(arr)

		endTime := time.Now()
		executionTime := endTime.Sub(startTime)

		fmt.Printf("Input size: %d, Steps: %d, Execution time: %s\n", size, steps, executionTime)
	}
}
