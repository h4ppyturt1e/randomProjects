from types import WrapperDescriptorType


CUR_BILL = 0
CUR_ITEM_LIST = 1

def createLists():
    # filename = input("Enter file name: ")
    filename = "tnt_receipt.txt"
    
    with open(filename) as f:
        data = [line.rstrip() for line in f.readlines()]
    
    sections = {}
    
    for line in data:
        if line == "":
            continue
        elif line[0] == "=":
            header = line.strip("==")
            sections[header] = []
            continue
        else:
            item_data = line.split(", ")
            item_data[1] = float(item_data[1])
            item_data = tuple(item_data)
            sections[header].append(item_data)
    
    return sections
            

def divideBill(sections):    
    entire_bill = []
    [[entire_bill.append(item) for item in sections[sect]] for sect in sections]
    full_bill = 0
    
    for _, price in entire_bill:
        full_bill += price
        
    print(f"\nFull bill: ${full_bill}")
    
    people_dict = {}
    
    cur_person = input("\nEnter the first person's name: ")
    people_dict[cur_person] = [0, []]

    while True:
        cur_person = input("Enter the next person's name [Enter nothing to end]: ")
        if cur_person == "":
            break
        else:
            people_dict[cur_person] = [0, []]
        
    for cur_person in people_dict:
        print(f"\nCurrent person is {cur_person}.")
        for sect in sections:
            for item_data in sections[sect]:
                item_name, item_price = item_data
                isBought = input(f"Did {cur_person} purchase \"{item_name}\" for ${item_price}? [y/n]")

                if isBought.lower() in ["y", "yes"]:
                    people_dict[cur_person][CUR_BILL] += item_price
                    people_dict[cur_person][CUR_ITEM_LIST].append(item_data)
                    print(f"Added to {cur_person}'s bill, currently at ${people_dict[cur_person][CUR_BILL]}")
                
            for item in people_dict[cur_person][CUR_ITEM_LIST]:
                try:
                    sections[sect].remove(item)
                except:
                    continue
            
    shared_bill = [0, []]
    
    print("\nThe rest of the items will be included in the shared bill.")
    for sect in sections:
        for item_data in sections[sect]:
            item_name, item_price = item_data
            shared_bill[CUR_BILL] += item_price
            shared_bill[CUR_ITEM_LIST].append(item_data)
            print(f"\"{item_name}\" was added to the shared bill for ${item_price}.\nTotal shared bill is currently at ${shared_bill[0]}.")
    
    print(f"\nFinal bill for everyone:")
    shared_divided = shared_bill[CUR_BILL] / len(people_dict)
    print(f"Shared: ${shared_divided} per person. [${shared_bill[CUR_BILL]} / {len(people_dict)}]")
    for cur_person in people_dict:
        cur_person_bill = people_dict[cur_person][CUR_BILL] + shared_divided
        print(f"{cur_person}: ${people_dict[cur_person][CUR_BILL]} + ${shared_divided} = ${cur_person_bill}")
    print(f"Full bill: ${full_bill}")
    
    people_dict["Shared"] = shared_bill
    
    return people_dict
    
    
def writeBill(people_dict):
    filename = input("Enter output file name: ")    
    shared_bill = people_dict.pop("Shared")
    shared_divided = shared_bill[CUR_BILL] / len(people_dict)
    
    with open(filename, "w") as f:
        f.write(f"Shared bill:\n")
        for item_name, item_price in shared_bill[CUR_ITEM_LIST]:
            f.write(f"\"{item_name}\": ${item_price}\n")
        f.write(f"\nShared bill divided: ${shared_divided} [${shared_bill[CUR_BILL]} / {len(people_dict)}]\n\n")
        
        for cur_person in people_dict:
            cur_person_bill = people_dict[cur_person][CUR_BILL] + shared_divided
            f.write(f"{cur_person}'s bill:\n")
            for item_name, item_price in people_dict[cur_person][CUR_ITEM_LIST]:
                f.write(f"\"{item_name}\": ${item_price}\n")
            f.write(f"Total: ${people_dict[cur_person][CUR_BILL]} + ${shared_divided} = ${cur_person_bill}\n\n")
            
        
def main():
    try:
        sections = createLists()
    except FileNotFoundError:
        print("File not found, try again.")
        main()
    
    if input("Do you want to view the full receipt? [y/n]").lower() in ["y", "yes"]:
        for sect in sections:
            print(f"\n{sect:}\n======================================")
            for item_name, item_price in sections[sect]:
                print(f"{item_name}: ${item_price}")

    people_dict = divideBill(sections)

    writeBill(people_dict)
    
        
if __name__ == '__main__':
    main()


    