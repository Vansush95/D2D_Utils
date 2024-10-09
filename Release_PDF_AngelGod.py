import pikepdf
import os
import pyfiglet


# Function to display the cool banner with greetings
def display_banner():
    banner = pyfiglet.figlet_format("AngeL God", font="slant")
    print(banner)
    print("👼 Welcome, AngeL God! The Breaker of Prime Dragon Force! 👼\n")

    # Greeting in 5 different languages
    greetings = {
        "English": "Hello, AngeL God!",
        "Japanese": "こんにちは、天使の神様！",
        "French": "Bonjour, AngeL Dieu !",
        "Spanish": "¡Hola, Dios Ángel!",
        "German": "Hallo, Engel Gott!"
    }
    
    for language, greeting in greetings.items():
        print(f"{language}: {greeting}")
    
    print("\nLet's open the gate of hell today!\n")

def main():
    
    #Display Banner
    display_banner()
    
    # Ask for the full path of the PDF file
    pdf_path = input("Please enter the full path of the PDF file: ")

    # Create the output path in the same directory with "_unrestricted" appended to the filename
    output_path = os.path.join(
        os.path.dirname(pdf_path),
        f"{os.path.splitext(os.path.basename(pdf_path))[0]}_unrestricted.pdf"
    )

    try:
        # Open the PDF file
        with pikepdf.open(pdf_path) as pdf:
            # Remove all usage restrictions
            pdf.save(output_path)

        print(f"The PDF has been saved without restrictions as '{output_path}'.")

    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == "__main__":
    main()
