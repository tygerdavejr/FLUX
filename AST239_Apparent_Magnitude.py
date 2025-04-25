"""
David Vance
Astronomy 239 Independent Study
Calculate Apparent Magnitude
2 April 2025
"""

import math

def calculate_apparent_magnitude(flux, reference_flux=1.0):
    """
    Calculate the apparent magnitude of a star given its flux and a reference flux.
    
    Parameters:
    flux (float): Measured flux of the star (in arbitrary units)
    reference_flux (float): Flux of reference star (default is 1.0 for simplicity)
    
    Returns:
    float: Apparent magnitude of the star
    """
    # I would also like to include range checks.  We have 0 as the min but I don't know what the
    # max value for flux would be and want to set that.  I'm a big fan of input validation.

    maxflux = 100


    while flux <= maxflux:

        try:
            # Check if inputs are valid
            if flux <= 0 or reference_flux <= 0:
                raise ValueError("Flux values must be positive")
            
            # Calculate magnitude using the formula: m = -2.5 * log10(F/F0)
            magnitude = -2.5 * math.log10(flux / reference_flux)
            return round(magnitude, 3)
    
        except ValueError as e:
            return f"Error: {e}"

    else:
        return f"Error: flux too high"

def main():
    print("Apparent Magnitude Calculator")
    print("---------------------------")
    
    try:
        # Get user input
        star_flux = float(input("Enter the star's flux (in arbitrary units): "))
        ref_flux = float(input("Enter the reference flux (press Enter for default 1.0): ") or 1.0)
        
        # Calculate and display result
        result = calculate_apparent_magnitude(star_flux, ref_flux)
        if isinstance(result, str):  # Check if result is an error message
            print(result)
        else:
            print(f"The apparent magnitude is: {result}")
            
    except ValueError:
        print("Error: Please enter valid numerical values")

if __name__ == "__main__":
    main()