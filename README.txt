2048 :

    Instructions :
        1.First Enter the Name in the TextBox on the left Bottom.
        2.Then click Start Button to start the Game.
        3.After this use Right, Left, Up, Down buttons to play the game.
        4.The text box below the Start button shows if the Game is Won/Lost or whether the move is valid or Invalid.
        5.Whenever we want to exit click on the exit button to leave the game.
        6.The score is also shown in the right side.
        7.If the game is over then automatically the score will be reset to zero as well as Restart button will be activated.
        8.The score board on the right bottom will be updated once the game is over.
        9.The game will be won if 2048 is scored in any button.

    Program Structure:
        1.Made a Grid of 4*4 to make all the operations on the Grid.
        2.On the right made a table to update high scores and display them in the table.
        3.I have written the functions for right left, up, down operations.All the functions will be called based on the buttons
          called.
        4.When no other operations are not possible then Game Over are indicated or if 2048 is made then You won is indicated and highscore is updated.
        5.Also I added some other features mostly making use of the Buttons and object oriented style in python.
        6.I have tried to write every possible operations in terms of member functions.

    Packages Used:
        1. App(needed obviously)
        2. StringProperty, ListProperty, BooleanProperty, NumericProperty(Used to auto update the buttons and changes made to some variables in main and
                                                                          auto update them in kv file)
        3. BoxLayout is used for the Layout of the kivy window.
        4. Copy function is used only once to duplicate the list we have.
        5.Random is used to randomly add new numbers to the grid.
        6.log2 from math is used.
        7.Pickle is used to store a dictionary with high score and name of high scorer in binary format.In every game at the end the high scores are updated.
    Learnt :
        1.I have learnt how to adapt to a new UI or any other language and how to learn it quickly.
        2.I have learnt the importance of OOP and member functions and how easy it is while making Games where are objects concept is easy to think and implement.
        3.Using simple member functions but using them in a organised manner I think this is what makes python very powerful.Especially for UI.
        4.The kivy is also perfectly suitable for OOP and blends in properly.
        5.Also using Kv file gives us the advantage of changing the final outlook like colours and sizes to adjust again and again without disturbing
          main file where the logic is implemented.It basically separates logic from the Graphics or Interface part meaning both to act independantly.