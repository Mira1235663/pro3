def show_indentation():
    print("Level 0: no indentation")          # 0 spaces

    if True:
        print("Level 1: 4 spaces")            # 4 spaces
        
        if True:
            print("Level 2: 8 spaces")        # 8 spaces
            
            for i in range(2):
                print("Level 3: 12 spaces")   # 12 spaces
                
                if i == 1:
                    print("Level 4: 16 spaces")  # 16 spaces

show_indentation()