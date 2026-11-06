def calcPmt(P0, r , k, N):
    i = r / k
    n = k * N

    payment = P0 * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
    return payment


def amortizationReport(P0, r, k, N, filename="amortization_report.txt"):
    payment = calcPmt(P0, r, k, N)
    balance = P0
    total_interest = 0

    with open(filename, "w") as outfile:
        outfile.write("AMORTIZATION REPORT\n")
        outfile.write("_" * 75 + "\n")

        outfile.write(
            f"{'Payment' :<12}{'Amount':<15}"
            f"{'Interest':<15}{'Principal':<15}{'Balance':<15}\n"


        )

        outfile.write("_" * 75 + "\n")

        for period in range(1, k * N + 1):
            interest = balance * (r / k)
            principal = payment - interest
            balance = balance - principal
           
            total_interest += interest

            if balance < 0:
                balance = 0

            outfile.write(
                f"{period:<12}"
                f"${payment:<14.2f}"
                f"${interest:<14.2f}"
                f"${principal:<14.2f}"
                f"${balance:<14.2f}\n"
                
            )


            outfile.write("_" * 75 + "\n")
            outfile.write(f"Total interest: ${total_interest:.2f}\n")


        print(f"Amortization report saved successfully!")



def main():
    print("Loan Amortization Calculator")

    P0 = float(input("Enter the loan amount: "))
    r = float(input("Enter the annual interest rate (decimal): "))
    k = int(input("Enter payments per year: "))
    N = int(input("Enter the number of years: "))


    filename = input("Enter the output file name: ")

    amortizationReport(P0, r, k, N, filename)


if __name__ == "__main__":
    main()