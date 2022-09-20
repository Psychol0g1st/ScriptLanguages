def main():
    students = [
        [ 'David', 5, 4, 5 ],
        [ 'Anton', 4, 4, 5 ],
        [ 'Greta', 4, 3, 3 ],
        [ 'Dorina', 1, 2, 4 ],
        [ 'Betti', 4, 3, 5 ],
    ]
    row_heading = "| {name:<8s} | {math:<4s} | {physics:<6s} | {literature:<10s} |".format
    row = "| {student:<8s} | {math:4d} | {physics:7d} | {literature:10d} |".format

    print
    print(row_heading(name="Name", math="Math", physics="Physics", literature="Literature"))
    for s in students:
        print(row(student=s[0], math=s[1], physics=s[2], literature=s[3]))

if __name__ == "__main__":
    main()
