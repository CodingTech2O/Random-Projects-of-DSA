import random
import time
import os
import sys

# Terminal rendering settings
HEIGHT = 20
WIDTH = 50
DELAY = 0.03

# ANSI Color Codes
CYAN = "\033[96m"
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"
CLEAR = "\033[H\033[J"

def generate_array():
    return [random.randint(1, HEIGHT) for _ in range(WIDTH)]

def draw(array, active_indices=(), sorted_indices=set(), algo_name=""):
    # Move cursor to top-left instead of clearing full screen to eliminate flicker
    sys.stdout.write("\033[H")
    sys.stdout.write(f"Sorting Visualizer — {algo_name}\n")
    sys.stdout.write("=" * WIDTH + "\n\n")

    # Render bars vertically from top to bottom
    for level in range(HEIGHT, 0, -1):
        line = []
        for i, val in enumerate(array):
            if val >= level:
                if i in active_indices:
                    line.append(f"{RED}█{RESET}")
                elif i in sorted_indices:
                    line.append(f"{GREEN}█{RESET}")
                else:
                    line.append(f"{CYAN}█{RESET}")
            else:
                line.append(" ")
        sys.stdout.write("".join(line) + "\n")

    sys.stdout.write("\n" + "=" * WIDTH + "\n")
    sys.stdout.flush()

def bubble_sort(array):
    n = len(array)
    sorted_set = set()
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

            draw(array, active_indices=(j, j + 1), sorted_indices=sorted_set, algo_name="Bubble Sort")
            time.sleep(DELAY)

        sorted_set.add(n - i - 1)
    draw(array, sorted_indices=set(range(n)), algo_name="Bubble Sort (Complete)")

def selection_sort(array):
    n = len(array)
    sorted_set = set()
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j
            draw(array, active_indices=(i, j, min_idx), sorted_indices=sorted_set, algo_name="Selection Sort")
            time.sleep(DELAY / 2)

        array[i], array[min_idx] = array[min_idx], array[i]
        sorted_set.add(i)

    draw(array, sorted_indices=set(range(n)), algo_name="Selection Sort (Complete)")

def main():
    sys.stdout.write(HIDE_CURSOR)
    sys.stdout.write(CLEAR)
    try:
        arr = generate_array()
        draw(arr, algo_name="Initial Array")
        time.sleep(1)

        bubble_sort(arr)
        time.sleep(2)

        arr = generate_array()
        selection_sort(arr)
        time.sleep(2)
    finally:
        sys.stdout.write(SHOW_CURSOR)
        print("\nDone!")

if __name__ == "__main__":
    main()