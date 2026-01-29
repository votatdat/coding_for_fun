package main

import (
	"fmt"
	"math/rand"
	"strings"
	"time"
)

func printFunc(ss ...string) <-chan string {
	c := make(chan string)

	go func() {
		defer close(c)
		for i := 0; ; i++ {
			for _, s := range ss {
				c <- fmt.Sprintf("===== %s %d ====", s, i)
				time.Sleep(time.Duration((rand.Intn(8)*100 + 200)) * time.Millisecond)
			}

		}
	}()

	return c
}

func fanIn(chan1, chan2 <-chan string) <-chan string {
	c := make(chan string, 10)
	go func() {
		for {
			select {
			case s := <-chan1:
				c <- s
			case s := <-chan2:
				c <- s
			}
		}
	}()

	return c
}

func main() {

	first := printFunc("Ann", "Ane", "Anie")
	second := printFunc("Ben")

	names := fanIn(first, second)

	// for name := range names {
	// 	fmt.Println(name)
	//     if strings.Contains(name, "30") {
	// 		return
	// 	}
	// }

	for i := 0; i <= 60; i++ {
		name := <-names
		fmt.Println(name)
		if strings.Contains(name, "30") {
			return
		}
	}

	// time.Sleep(10 * time.Second)
}
