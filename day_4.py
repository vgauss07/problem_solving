"""
The Challenge:
    - 5 favorite songs: A, B, C, D, and E
    - The app has 4 buttons:
        - 1: Moves first song to the end of the playlist
        - 2: Moves the last song to the beginning of the playlist
        - 3: Swaps the first 2 songs of the playlist i.e
                A, B, C, D, E changes to B, A, C, D, E
        - 4: Plays the playlist

    Input:
        - Line 1: The number of a button
        - Line 2: number of times the user hit the button.
        - Line 3: the numnber of a button
        - Line 4: the number of times the user hit the button

    Output:
        - the order of songs in the playlist after all the button 
        - presses.

Solution:
    - Have a plan:
        Step 1: input statements for 4 buttons
        Step 2: input statements for the number of times the button
                was hit.
        Step 3: Run a loop!
        Step 4: return values.
"""

songs = 'ABCDE'

buttons_ = 0
while buttons_ != 4: # while loop continues as long as 4 hasnt been pressed
    buttons_ = int(input("Enter the button: "))
    frequency_ = int(input("How many times was that button hit: "))
    for i in range(frequency_):
        if buttons_ == 1:
        # button 1
        # the list becomes
        # B C D E A
            song = songs[1:] + songs[0]
        elif buttons_ == 2:
        # button 2
        # moves the last song
        # to the beginning of the
        # playlist
        # E A B C D
            song = songs[-1:] + songs[0:-1]
        elif buttons_ == 3:
        # button 3
        # swaps the first two
        # songs
        # A B C D E => B A C D E
            song = songs[1] + songs[0] + songs[2:]
    output = ''  # output songs with spaces
    for song in songs:
        output = output + song + ' '
print(output[:-1])




