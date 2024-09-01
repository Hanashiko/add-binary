def addBinary(a: str, b: str) -> str:
    decimal_a: int = int(a, 2)
    decimal_b: int = int(b, 2)
    added: int = decimal_a + decimal_b
    return f"{added:b}"

def main() -> None:
    print(addBinary("11", "1"))
    
if __name__ == "__main__":
    main()