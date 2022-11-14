def convert_mass_to_energy(mass:int)->int:
    c=300000000
    energy= mass*c*c
    return str(energy)
def main():
    user_input=int(input("m: "))
    print(f"E: {convert_mass_to_energy(user_input)}")
main()