package main

import "testing"

func benchBuf(b *testing.B, buf int) {
    for n := 0; n < b.N; n++ {
        ch := make(chan int, buf)
        done := make(chan struct{})

        go func() {
            for i := 0; i < 1000; i++ {
                <-ch
            }
            close(done)
        }()

        for i := 0; i < 1000; i++ {
            ch <- i
        }
        <-done
    }
}

func BenchmarkBuf1(b *testing.B)  { benchBuf(b, 1) }
func BenchmarkBuf4(b *testing.B)  { benchBuf(b, 4) }
func BenchmarkBuf16(b *testing.B) { benchBuf(b, 16) }
