# AI Final Project – 8 Puzzle Solver using A*

## Description
This project implements the A* search algorithm to solve the 8-puzzle problem.

The 8-puzzle is a 3×3 board with 8 numbered tiles and one empty space. 
The goal is to rearrange the tiles into the correct order using the smallest number of moves.

In this project, heuristic functions such as Manhattan Distance and Misplaced Tiles are used 
to guide the search and improve performance.

## Features
- A* search algorithm implementation
- Two heuristics:
  - Manhattan Distance
  - Misplaced Tiles
- Solves easy and medium puzzle configurations
- Detects unsolvable cases

## Repository Structure

dataset/ → example puzzle configurations (used for testing)  
code/ → Python implementation of the solver  
proposal/ → project proposal document  
report/ → final project report  
results/ → screenshots of outputs  

## How to Run

```bash
python astar_8puzzle.py
