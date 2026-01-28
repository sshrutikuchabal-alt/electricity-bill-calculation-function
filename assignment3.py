def calculate_electricity_bill(units):
    bill = 0
    
    # First 100 units
    if units <= 100:
        bill = units * 2
    else:
        bill = 100 * 2
        units -= 100
        
        # Next 100 units
        if units <= 100:
            bill += units * 4
        else:
            bill += 100 * 4
            units -= 100
            
            # Above 200 units
            bill += units * 6
    
    return bill


# Example usage:
print(calculate_electricity_bill(250))  # Output for 250 units
