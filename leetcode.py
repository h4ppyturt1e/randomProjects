def isMatch(s: str, p: str) -> bool:
        """
        '.' -> any char
        '*' -> any multiple of the element before
        """
        
        ruleSet = []
        
        prevLetter = ""
        for i in range(len(p)):
            letter = p[i]
            if letter == '*':
                del ruleSet[-1]
                ruleSet.append(prevLetter + letter)
            else:
                ruleSet.append(letter)
            prevLetter = letter
            
        
        print(f"\n---------------------------------------------------\n\ns: {s}, p: {p}")
        
        sIter = iter(list(s))
        
        
        curLetter = next(sIter)
        c = 1

        for i in range(len(ruleSet)):
            checkedLetter = ruleSet[i]
            print(f"CUR    : {curLetter}[{c}]")
            print(f"CHECKED: {checkedLetter}[{i+1}]")
            if len(checkedLetter) > 1:    # contains *
                checkedLetter = checkedLetter[0]
                if checkedLetter != '.':
                    while checkedLetter == curLetter:
                        try:
                            curLetter = next(sIter)
                            c += 1
                            print(f"        WHILE: {curLetter}[{c}]")
                        except:
                            print(f"        BREAK OUT OF _*")
                            break
                else:                     # contains .*
                    try:
                        print(f"next: {ruleSet[i+1]}")
                        nextSingle = ""
                        for rule in ruleSet[i+1:]:
                            if len(rule) == 1:
                                nextSingle = rule
                                break
                        try:
                            if nextSingle == ruleSet[i+1]:  # RIGHT HERE BOSS!
                                print()
                                continue
                            curLetter = next(sIter)
                            c += 1
                            print(f"\nCUR    : {curLetter}[{c}]")
                            print(f"CHECKED: {checkedLetter}[{i+1}]")
                            while (nextSingle != "" and curLetter != nextSingle) or '*' not in ruleSet[i+1]:
                                curLetter = next(sIter)
                                c += 1
                                print(f"\nCUR    : {curLetter}[{c}]")
                                print(f"CHECKED: {checkedLetter}[{i+1}]")
                                print(f"        LOOP IN .*")
                        except:
                            pass
                    except:
                        return True

            else:                   # otherwise, single letter
                if checkedLetter != '.':
                    if checkedLetter != curLetter:
                        print("MISMATCH!!")
                        return False    # if letter doesn't match, pattern doesnt exist
                    
                    try:
                        ruleSet[i+1]

                        curLetter = next(sIter)
                        c += 1
                    except IndexError:
                        pass
                    except StopIteration:
                        for x in ruleSet[i+1:]:
                            if '*' not in x:
                                print("NO MATCH, STOPPED ITERATION!!")
                                return False
                else:
                    try:
                        curLetter = next(sIter)
                        c += 1
                        ruleSet[i+1]
                    except IndexError:
                        print("NO MATCH, STRING OVERFLOW!!")
                        return False
                    except StopIteration:
                        if (ruleSet[i+1:] != []) and ('*' not in ruleSet[i+1]):
                            print("NO MATCH, PATTERN OVERFLOW!!")
                            return False
                print("=========SINGLE!!!!=========")
            print()              
        
        try:
            next(sIter)
            print("NO MATCH / NOT FULL MATCH!!")
            return False
        except:
            print("MATCHED!!")
            return True


if __name__ == '__main__':
    result = []
    result.append((isMatch("aa", "a") == False))
    result.append((isMatch("aa", "a*") == True))
    result.append((isMatch("ab", ".*") == True))
    result.append((isMatch("aab", "c*a*b") == True))
    result.append((isMatch("mississippi", "mis*is*p*.") == False))
    result.append((isMatch("mississippi", "mis*is*ip*.") == True))
    result.append((isMatch("aaa", "aaaa") == False))
    result.append((isMatch("aaa", "a.a") == True))
    result.append((isMatch("aaa", ".*") == True))
    result.append((isMatch("ab", ".*c") == False))
    result.append((isMatch("aa", ".") == False))
    result.append((isMatch("a", "ab*") == True))
    result.append((isMatch("a", "ab*a") == False))
    result.append((isMatch("bbbba", ".*a*a") == True))
    result.append((isMatch("a", ".*..a*") == False))
    result.append((isMatch("ab", ".*..") == True))
    result.append((isMatch("ab", ".*..c*") == True))
    result.append((isMatch("baaab", "ba*b") == True))
    result.append((isMatch("aasdfasdfasdfasdfas", "aasdf.*asdf.*asdf.*asdf.*s") == True))
    result.append((isMatch("baaa", "b.*a") == True))

    print()
    print(result)
    print()
    print("Something's wrong..." if any([not x for x in result]) else "Kanpeki da!")
