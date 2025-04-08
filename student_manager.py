import pandas as pd
import matplotlib.pyplot as plt

ch = "Y"
df = None  # Initialize df

while ch == "Y":
    print("\n" + "="*40)
    print("Student Records Management System")
    print("="*40)
    print("1.  Read CSV file")
    print("2.  Show all records")
    print("3.  Show first 3 records")
    print("4.  Show last 3 records")
    print("5.  Show names of failed students")
    print("6.  Add new row")
    print("7.  Delete row")
    print("8.  Show result using line graph")
    print("9.  Show result using bar graph")
    print("10. Save data into CSV file")
    print("11. Show top scorers")
    print("12. Calculate class average")
    print("13. Sort records by marks")
    print("14. Search for a student")
    print("15. Show highest & lowest marks")
    print("16. Show grade distribution (Pie Chart)")
    print("17. Show pass vs fail (Pie Chart)")
    print("18. Line chart of top scorers")
    print("19. Bar chart of top scorers")
    print("20. Line chart of lowest scorers")
    print("21. Bar chart of lowest scorers")
    print("22. Combined trend of marks")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        try:
            df = pd.read_csv("test.csv")
            print("File opened successfully!")
        except FileNotFoundError:
            print("Error: CSV file not found!")

    elif choice in range(2, 23) and df is None:
        print("Error: Please load the CSV file first!")

    elif choice == 2:
        print(df)

    elif choice == 3:
        print(df.head(3))

    elif choice == 4:
        print(df.tail(3))

    elif choice == 5:
        failed_students = df[df["marks"] < 40]["name"]
        if failed_students.empty:
            print("No students have failed.")
        else:
            print("Failed students:\n", failed_students)

    elif choice == 6:
        r = int(input("Enter roll no: "))
        n = input("Enter name: ")
        m = int(input("Enter marks: "))
        new_row = pd.DataFrame({"roll": [r], "name": [n], "marks": [m]})
        df = pd.concat([df, new_row], ignore_index=True)
        print("Record added successfully")

    elif choice == 7:
        r = int(input("Enter roll no to delete: "))
        if r in df["roll"].values:
            df = df[df["roll"] != r]
            print("Record deleted successfully")
        else:
            print("Error: Roll number not found!")

    elif choice == 8:
        plt.plot(df["roll"], df["marks"], marker='o', linestyle='-', color='green')
        plt.title("Result (Line Graph)")
        plt.xlabel("Roll Number")
        plt.ylabel("Marks")
        plt.grid(True)
        plt.show()

    elif choice == 9:
        plt.bar(df["roll"], df["marks"], color='blue')
        plt.title("Result (Bar Graph)")
        plt.xlabel("Roll Number")
        plt.ylabel("Marks")
        plt.show()

    elif choice == 10:
        df.to_csv("test.csv", index=False)
        print("File saved successfully")

    elif choice == 11:
        top_score = df["marks"].max()
        top_scorers = df[df["marks"] == top_score]
        print("Top Scorers:\n", top_scorers)

    elif choice == 12:
        avg_marks = df["marks"].mean()
        print(f"Class Average Marks: {avg_marks:.2f}")

    elif choice == 13:
        print(df.sort_values(by="marks", ascending=False))

    elif choice == 14:
        search_name = input("Enter student name to search: ").strip().lower()
        result = df[df["name"].str.lower() == search_name]
        if result.empty:
            print("No student found with that name.")
        else:
            print(result)

    elif choice == 15:
        print(f"Highest Marks: {df['marks'].max()}")
        print(f"Lowest Marks: {df['marks'].min()}")

    elif choice == 16:
        def get_grade(marks):
            if marks >= 90: return "A"
            elif marks >= 75: return "B"
            elif marks >= 60: return "C"
            elif marks >= 40: return "D"
            else: return "Fail"
        df["Grade"] = df["marks"].apply(get_grade)
        grade_counts = df["Grade"].value_counts()
        plt.figure(figsize=(6, 6))
        plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%')
        plt.title("Grade Distribution")
        plt.show()

    elif choice == 17:
        pass_count = len(df[df["marks"] >= 40])
        fail_count = len(df[df["marks"] < 40])
        plt.pie([pass_count, fail_count], labels=["Pass", "Fail"], autopct='%1.1f%%', colors=["green", "red"])
        plt.title("Pass vs Fail")
        plt.show()

    elif choice == 18:
        top_score = df["marks"].max()
        top_df = df[df["marks"] == top_score]
        plt.plot(top_df["roll"], top_df["marks"], marker='o', color='purple')
        plt.title("Top Scorers (Line Chart)")
        plt.xlabel("Roll No")
        plt.ylabel("Marks")
        plt.grid(True)
        plt.show()

    elif choice == 19:
        top_score = df["marks"].max()
        top_df = df[df["marks"] == top_score]
        plt.bar(top_df["roll"], top_df["marks"], color='purple')
        plt.title("Top Scorers (Bar Chart)")
        plt.xlabel("Roll No")
        plt.ylabel("Marks")
        plt.show()

    elif choice == 20:
        low_score = df["marks"].min()
        low_df = df[df["marks"] == low_score]
        plt.plot(low_df["roll"], low_df["marks"], marker='x', color='red')
        plt.title("Lowest Scorers (Line Chart)")
        plt.xlabel("Roll No")
        plt.ylabel("Marks")
        plt.grid(True)
        plt.show()

    elif choice == 21:
        low_score = df["marks"].min()
        low_df = df[df["marks"] == low_score]
        plt.bar(low_df["roll"], low_df["marks"], color='red')
        plt.title("Lowest Scorers (Bar Chart)")
        plt.xlabel("Roll No")
        plt.ylabel("Marks")
        plt.show()

    elif choice == 22:
        plt.plot(df["roll"], df["marks"], marker='o', color='teal')
        plt.title("Overall Score Trend")
        plt.xlabel("Roll Number")
        plt.ylabel("Marks")
        plt.grid(True)
        plt.show()

    else:
        print("Invalid choice! Please enter a number between 1–22.")

    ch = input("\nDo you want to continue (Y/N)? ").upper()
