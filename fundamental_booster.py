print("Welcome to the Interactive personal Data Collector!")

name=input("Please enter your name:")
age=int(input("please enter your age:"))
height=float(input("please enter your height in meters:"))
fav_num=int(input("please enter your favourite number:"))

print("Thank you! Here is the information we collected:")

print(f"Name:{name}(Type):{type (name)}),Memory addres:{id(name)}")
print(f"Age:{age}(Type):{type (age)}),Memory addres:{id(age)}")
print(f"Height:{height}(Type):{type (height)}),Memory addres:{id(height)}")
print(f"fav_num:{fav_num}(Type):{type (fav_num)}),Memory addres:{id(fav_num)}")

current_year=2026

birth_year=current_year-age

print(f"your birth year is approximately:{birth_year}(based on your age of 18)")

print("Thank you for using the Personal Data Collector. Goodbye!")






