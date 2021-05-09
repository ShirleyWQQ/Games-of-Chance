import random

money = 100


def flip_coin(guess, bet_amount):
  num = random.randint(1, 2)
  if ((num == 1 and guess == 'Head') or 
  (num == 2 and guess == 'Tail')):
    print("You get the {temp} and you guessed right! You won {money} dollars.".format(temp = guess, money = bet_amount))
    return bet_amount
  elif guess == 'Head':
    print("You get the Tail and you guessed wrong! You lost {money} dollars.".format(temp = guess, money = bet_amount))
  elif guess == 'Tail':
    print("You get the Head and you guessed wrong! You lost {money} dollars.".format(temp = guess, money = bet_amount))
  return -1 * bet_amount



def cho_han(guess, bet_amount):
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  if (dice1 + dice2) % 2 == 0:
    if guess == 'Even':
      print("You guessed right! The total point is {amount} and you won {money} dollars.".format(amount = dice1 + dice2, money = bet_amount))
      return bet_amount
    print("You guessed wrong! The total point is {amount} and you lose {money} dollars.".format(amount = dice1 + dice2, money = bet_amount))
    return -1 * bet_amount
  if (dice1 + dice2) % 2 == 1:
    if guess == 'Odd':
      print("You guessed right! The total point is {amount} and you won {money} dollars.".format(amount = dice1 + dice2, money = bet_amount))
      return bet_amount
    print("You guessed wrong! The total point is {amount} and you lose {money} dollars.".format(amount = dice1 + dice2, money = bet_amount))
    return -1 * bet_amount



def pick_cards(bet_amount):
  cards = []
  for i in range(4):
    cards += [i for i in range(1, 14)]
  user_pick = random.choice(cards)
  print("You picked card {num}.".format(num = user_pick))
  cards.remove(user_pick)
  print(cards)
  machine_pick = random.choice(cards)
  print("The machine picked card {num}.".format(num = machine_pick))
  if user_pick == machine_pick:
    return 0
  elif user_pick > machine_pick:
    print("You win! Your point is {user} and machine's point is {machine}. You win {money} dollars.".format(user = user_pick, machine = machine_pick, money = bet_amount))
    return bet_amount
  else:
    print("You lost! Your point is {user} and machine's point is {machine}.".format(user = user_pick, machine = machine_pick))
    return -1 * bet_amount



# double zero wheel roulette implementation
def double_zero_roulette(bet_amount, money):
  print('Welcome to double zero wheel Roulette! How do you want to bet for this round?')
  print('1: red or black')
  print('2: even or odd')
  print('3: bet by single number')
  print('4: bet by row')
  print('5: bet by column')
  print("Enter your choice:")
  val = input()
  temp = [i for i in range(1, 37)]
  board = []
  for num in temp:
    board.append(str(num))
  board.append('0')
  board.append('00')
  #print(board)
  spin_result = random.choice(board)
  if int(val) == 1:
    print("Enter either 'Red' or 'Black' as your bet:\n")
    guess = input()
    while guess != 'Red' and guess != 'Black':
      print("Please enter either 'Red' or 'Black' for your guess. Pay attention to the capitalization!")
      guess = input()
    gain = red_or_black(spin_result, guess, bet_amount)
    money += gain
    print('Your current balance is {amount} dollars.'.format(amount = money))
    return money
  elif int(val) == 2:
    guess = input("Enter either 'Odd' or 'Even' as your bet:\n")
    while guess != 'Even' and guess != 'Odd':
      print("Please enter either 'Even' or 'Odd' for your guess. Pay attention to the capitalization!")
      guess = input()
    gain = even_or_odd(spin_result, guess, bet_amount)
    money += gain
    print('Your current balance is {amount} dollars.'.format(amount = money))
    return money
  elif int(val) == 3:
    guess = input("Enter a number from '0' to '36' or '00' as your bet:")
    gain = bet_by_single(spin_result, guess, bet_amount)
    money += gain
    print('Your current balance is {amount} dollars.'.format(amount = money))
    return money
  elif int(val) == 4:
    guess = input("Enter a number from '1' to '12' as the row number for your bet:")
    gain = bet_by_row(spin_result, guess, bet_amount)
    money += gain
    print('Your current balance is {amount} dollars.'.format(amount = money))
    return money
  elif int(val) == 5:
    guess = input("Enter a number from '1' to '3' as the column number for your bet:")
    gain = bet_by_column(spin_result, guess, bet_amount)
    money += gain
    print('Your current balance is {amount} dollars.'.format(amount = money))
    return money

  

def even_or_odd(spin_result, guess, bet_amount):
  if (spin_result == '0' or spin_result == '00'):
    print('You lost! You spinned ' + spin_result + ' and you lost {money} dollars.'.format(money = bet_amount))
    return -1 * bet_amount
  elif (guess == 'Even' and int(spin_result) % 2 == 0) or (guess == 'Odd' and int(spin_result) % 2 == 1):
    print('You won! You spinned ' + spin_result + ' and you won {money} dollars.'.format(money = bet_amount))
    return bet_amount
  else:
    print('You lost! You spinned ' + spin_result + ' and you lost {money} dollars.'.format(money = bet_amount))
    return -1 * bet_amount



def red_or_black(spin_result, guess, bet_amount):
  red_nums = ['1', '3', '5', '7', '9', '11', '14', '16', '18', '19', '21', '23', '25', '27', '30', '32', '34', '36']
  black_nums = ['2', '4', '6', '8', '10', '11', '13', '15', '17', '20', '22', '24', '26', '28', '29', '31', '33', '35']
  if (spin_result in red_nums and guess == 'Red') or (spin_result in black_nums and guess == 'Black') :
    print('You spinned {spin} and it is {guess}. You won {money} dollars!'.format(spin = spin_result, guess = guess, money = bet_amount))
    return bet_amount
  print('You spinned {spin} and it is not {guess}. You lost {money} dollars!'.format(spin = spin_result, guess = guess, money = bet_amount))
  return -1 * bet_amount



def bet_by_single(spin_result, guess, bet_amount):
  if spin_result == guess:
    print('You win! You spinned ' + spin_result + ' and you won {money} dollars.'.format(money = 35 * bet_amount))
    return 35 * bet_amount
  else:
    print('You lose! You spinned ' + spin_result + ' and you lost {money} dollars.'.format(money = bet_amount))
    return -1 * bet_amount



def bet_by_row(spin_result, guess, bet_amount):
  row_1 = ['1', '2', '3']
  row_2 = ['4', '5', '6']
  row_3 = ['7', '8', '9']
  row_4 = ['10', '11', '12']
  row_5 = ['13', '14', '15']
  row_6 = ['16', '17', '18']
  row_7 = ['19', '20', '21']
  row_8 = ['22', '23', '24']
  row_9 = ['25', '26', '27']
  row_10 = ['28', '29', '30']
  row_11 = ['31', '32', '33']
  row_12 = ['34', '35', '36']
  if spin_result == '00' or spin_result == '0':
    print('You lose! You spinned ' + spin_result + ' and it is not in any of the rows on the board. You lost {money} dollars.'.format(num = int(guess), money = bet_amount))
    return -1 * bet_amount
  if ((spin_result in row_1 and guess == '1') or 
  (spin_result in row_2 and guess == '2') or 
  (spin_result in row_3 and guess == '3') or 
  (spin_result in row_4 and guess == '4') or 
  (spin_result in row_5 and guess == '5') or 
  (spin_result in row_6 and guess == '6') or 
  (spin_result in row_7 and guess == '7') or 
  (spin_result in row_8 and guess == '8') or 
  (spin_result in row_9 and guess == '9') or 
  (spin_result in row_10 and guess == '10') or 
  (spin_result in row_11 and guess == '11') or (spin_result in row_12 and guess == '12')):
    print('You win! You spinned ' + spin_result + ' and it is in row {num}. You won {money} dollars.'.format(num = int(guess), money = 11 * bet_amount))
    return 11 * bet_amount
  else:
    print('You lose! You spinned ' + spin_result + ' and it is not in row {num}. You lost {money} dollars.'.format(num = int(guess), money = bet_amount))
    return -1 * bet_amount



def bet_by_column(spin_result, guess, bet_amount):
  col_1 = ['1', '4', '7', '10', '13', '16', '19', '22', '25', '28', '31', '34']
  col_2 = ['2', '5', '8', '11', '14', '17', '20', '23', '26', '29', '32', '35']
  col_3 = ['3', '6', '9', '12', '15', '18', '21', '24', '27', '30', '33', '36']
  if spin_result == '00' or spin_result == '0':
    print('You lose! You spinned ' + spin_result + ' and it is not in any of the columns on the board. You lost {money} dollars.'.format(num = int(guess), money = bet_amount))
    return -1 * bet_amount
  if ((spin_result in col_1 and guess == '1') or (spin_result in col_2 and guess == '2') or 
  (spin_result in col_3 and guess == '3')):
   print('You win! You spinned ' + spin_result + ' and it is in column {num}. You won {money} dollars.'.format(num = int(guess), money = 2 * bet_amount))
   return 2 * bet_amount
  else:
    print('You lose! You spinned ' + spin_result + ' and it is not in column {num}. You lost {money} dollars.'.format(num = int(guess), money = bet_amount))
    return -1 * bet_amount


  
def casino():
  print('Welcome! Please enter the amount of money you would like to use to play this game.')
  initial_amount = int(input())
  current_balance = initial_amount
  while current_balance <= 0:
    print("You cannot bring a negative amount of money or no money into the casino, that's against the rules! Please enter a positive integer as the amount of money.")
    current_balance = input()
  print('Your initial amount is {money} dollars.'.format(money = current_balance))
  while int(current_balance) > 0:
    print('Continue (enter 1) or Exit (enter 2)?')
    num = input()
    if (num == '2'):
      break;
    elif (num == '1'):
      print('Which game would you like to play?')
      print('1: flip coins')
      print('2: Cho Han')
      print('3: Pick cards')
      print('4: Double Zero Roulette')
      choice = input()
      print('Enter the amount you want to bet:')
      bet_amount = int(input())
      while bet_amount > current_balance or bet_amount <= 0:
        print('Invalid bet amount, please enter a positive amount not greater that your current balance:')
        bet_amount = int(input())
      if choice == '1':
        print("Enter 'Head' or 'Tail' as you guess:")
        guess = input()
        while guess != 'Head' and guess != 'Tail':
          print("Please enter either 'Head' or 'Tail' for your guess. Pay attention to the capitalization!")
          guess = input()
        gain = flip_coin(guess, bet_amount)
        current_balance += gain
        print('Your current balance is {amount} dollars.'.format(amount = current_balance))
      elif choice == '2':
        print("Enter 'Even' or 'Odd' as you guess:")
        guess = input()
        while guess != 'Even' and guess != 'Odd':
          print("Please enter either 'Even' or 'Odd' for your guess. Pay attention to the capitalization!")
          guess = input()
        gain = cho_han(guess, bet_amount)
        current_balance += gain
        print('Your current balance is {amount} dollars.'.format(amount = current_balance))
      elif choice == '3':
        gain = pick_cards(bet_amount)
        current_balance += gain
        print('Your current balance is {amount} dollars.'.format(amount = current_balance))
      elif choice == '4':
        current_balance = double_zero_roulette(bet_amount, current_balance)
        #print('Your current balance is {amount} dollars.'.format(amount = current_balance))
  diff = current_balance - initial_amount
  if diff < 0:
    print('You lost {amount} dollars in total for this visit. Good luck next time!'.format(amount = abs(diff)))
  elif diff > 0:
    print('You won {amount} dollars in total for this visit. Good job!'.format(amount = diff))
  else:
    print('You didn\'t win or lose any money for this visit. Not interested in playing at all or highly skilled? Only you know the answer.')

#double_zero_roulette(35, 100)
casino()
