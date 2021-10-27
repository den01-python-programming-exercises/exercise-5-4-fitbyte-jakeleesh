from fit_byte import FitByte

def main():
    #write your code below this line
    assistant = FitByte(30, 60)

    percentage = 0.5

    while (percentage < 1.0):
        target = assistant.target_heart_rate(percentage)
        print("Target " + str((percentage * 100)) + "% of maximum: " + str(target))
        percentage = percentage + 0.1

if __name__ == '__main__':
    main()
