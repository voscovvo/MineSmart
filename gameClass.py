import pygame

from database_functions import *
from commonFunctions import *
from createSolutionTask import create_solution_task3
from displayClass import *
from solveNumHolder import draw_solvenum_holder3
from ui import *


class GameClass:
    def __init__(self):
        self.exitGame = 0
        self.quitFlag = 0

        self.level_id = 1
        self.level_name = db_get_level_name(1)
        self.player_id = 1
        self.player_name = db_get_player_name(1)
        self.player_current_round_score = 0

        self.DisplayInitialized = 0
        self.display = DisplayInfo()

        self.timer = pygame.time.Clock()
        self.frame_update_counter = 0
        self.game_round_messages_timer = 0

        self.is_round_timer_active = 0
        self.round_started_timer = 0
        self.round_timer_progress = 0
        self.round_timer_value = 0

        self.new_solution = None

        self.key_num = None
        self.keyInfo = None  # pygame.key.get_pressed()
        self.generate_new_solve_task = 0
        self.mouse_y = 0
        self.mouse_x = 0
        self.mouse_hover_y = 0
        self.mouse_hover_x = 0

        self.ui_surface = None
        self.game_round_surface = None
        self.game_round_messages = None

    def InitDisplay(self):
        self.display.CreateScreen()
        self.DisplayInitilized = 1

    def handle_player_inputs(self):

        self.key_num = None

        for event in pygame.event.get():
            # Check for player quitting
            if event.type == pygame.QUIT:
                self.quitFlag = 1
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = self.handle_mouse_click_from_event(event)
                if event.type == pygame.MOUSEMOTION:
                    self.handle_mouse_movement(event)
                #if event.type == pygame.KEYDOWN:
                    # self.keyUnicode = event.unicode
                    # if self.keyUnicode.isnumeric():
                    #     self.key_num = int(self.keyUnicode)
                    # else:
                    #     self.key_num = None

        self.keyInfo = pygame.key.get_pressed()
        k = self.keyInfo

        # if ESCAPE pressed - Quit Game
        if k[pygame.K_ESCAPE]:
            self.quitFlag = 1

        # READs 0-9 buttons pressed to self.key_num
        elif k[pygame.K_0] or k[pygame.K_KP0]:
            self.key_num = 0
        elif k[pygame.K_1] or k[pygame.K_KP1]:
            self.key_num = 1
        elif k[pygame.K_2] or k[pygame.K_KP2]:
            self.key_num = 2
        elif k[pygame.K_3] or k[pygame.K_KP3]:
            self.key_num = 3
        elif k[pygame.K_4] or k[pygame.K_KP4]:
            self.key_num = 4
        elif k[pygame.K_5] or k[pygame.K_KP5]:
            self.key_num = 5
        elif k[pygame.K_6] or k[pygame.K_KP6]:
            self.key_num = 6
        elif k[pygame.K_7] or k[pygame.K_KP7]:
            self.key_num = 7
        elif k[pygame.K_8] or k[pygame.K_KP8]:
            self.key_num = 8
        elif k[pygame.K_9] or k[pygame.K_KP9]:
            self.key_num = 9

        # SWITCHED by SPACE BAR: CHOOSE FIND NEW SOLVE TASK or WAIT
        elif k[pygame.K_SPACE]:
            if self.generate_new_solve_task == 0:
                self.generate_new_solve_task = 1  # FIND TASK
            else:
                self.generate_new_solve_task = 0  # WAIT for ANSWER
            pygame.time.delay(100)

        # START ROUND
        elif k[pygame.K_RETURN] or k[pygame.K_KP_ENTER]:
            self.round_started_timer = pygame.time.get_ticks()
            self.is_round_timer_active = 1
            self.player_current_round_score = 0
            self.generate_new_solve_task = 1

        # CHOOSE ACTIVE PLAYER
        elif k[pygame.K_F1]:
            self.player_id = 1
            self.player_name = db_get_player_name(self.player_id)
        elif k[pygame.K_F2]:
            self.player_id = 2
            self.player_name = db_get_player_name(self.player_id)
        elif k[pygame.K_F3]:
            self.player_id = 3
            self.player_name = db_get_player_name(self.player_id)
        elif k[pygame.K_F4]:
            self.player_id = 4
            self.player_name = db_get_player_name(self.player_id)

        else:

            pass

        # UPDATE MOUSE COORDs if RMB is pressed
        self.handle_mouse_click_from_get_pressed()

    def handle_mouse_movement(self, event):
        self.mouse_hover_x = event.dict["pos"][0]
        self.mouse_hover_y = event.dict["pos"][1]

    def handle_mouse_click_from_event(self, event):
        # Read location and which buttons are down...
        buttonPressed = event.dict["button"]
        mx = event.dict["pos"][0]
        my = event.dict["pos"][1]
        return mx, my

    def handle_mouse_click_from_get_pressed(self):
        self.mouse_x, self.mouse_y = 0, 0
        mouse_button = pygame.mouse.get_pressed()
        if mouse_button[0]:
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

    def update_game_timers(self):
        self.timer.tick(FPS)  #delay to match requested FPS value
        self.frame_update_counter += 1  #update game loop runs counter

        pygame.time.delay(self.game_round_messages_timer)  # Delay game as requested by Game messages events
        self.game_round_messages_timer = 0

    def draw_initial_layers(self):
        # if self.display.GetScreen() is not None:
        #     self.display.GetScreen().fill(BACKGROUND_COLOR)
        self.display.screen.fill(BACKGROUND_COLOR)

        # create User Interface Surface
        self.ui_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        #self.ui_surface.convert_alpha()
        # create Game Round Surface
        self.game_round_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        # create Game Round Surface
        self.game_round_messages = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

    def combine_all_game_layers(self):
        """ Draw all game surfaces to main screen"""
        self.display.screen.blit(self.ui_surface, (0, 0))  # UI layer
        self.display.screen.blit(self.game_round_surface, (0, 0))  # Game Round layer
        self.display.screen.blit(self.game_round_messages, (0, 0))  # Game Round layer

        pass

# ######################################------ MAIN  GAME LOOP STARTS HERE -------#################################
    def main_loop(self):
        if self.DisplayInitialized == 0:
            self.InitDisplay()  # display.set_mode... time.clock () - creates main screen surface

        mainloop_timer = pygame.time.get_ticks()
        self.player_current_round_score = 0

        generate_solution_animation_counter = 0
        solveNum_Action, solveNum_1, solveNum_2, solveNum_Result, blind, self.answer = "+", 0, 0, 0, 0, 0

        is_bonus_counter_active = 0
        bonus_started_timer = 0
        bonus_counter_progress = 0
        bonus_counter_value = 0

        # ----------------------------- If NOT QUIT loop START here -------------------------------------
        while not self.quitFlag:

            self.draw_initial_layers()    # Fill background color AND Draws all Standard Game Surfaces

            # Read Keyboard and mouse and React
            self.handle_player_inputs()
            mx, my = self.mouse_x, self.mouse_y
            key_pressed_num = self.key_num

            # Display SCORE and WHO PLAYS and which LEVEL
            coords = (WIDTH / 2 - 290, 80)
            draw_current_score_player_level(self.game_round_surface, coords,
                                            self.player_current_round_score,
                                            self.player_name,
                                            self.level_name)

            # Draw Buttons to choose player
            coords = (0, 0)
            self.player_id = draw_player_switch_buttons(self.ui_surface, coords, (mx, my), self.player_id)
            self.player_name = db_get_player_name(self.player_id)

            # Draw Buttons to choose Level
            coords = (0, 0)
            self.level_id = draw_level_switch_buttons(self.ui_surface, coords, (mx, my), self.level_id)
            self.level_name = db_get_level_name(self.level_id)

            # Draw PLayers Table scores
            coords = (WIDTH - 250, 100)
            draw_players_score_table_for_level(self.ui_surface, coords, self.level_id)

            # Draws Round timer
            draw_timer(self.game_round_surface, (50, 50), self.round_timer_progress, self.round_timer_value)

            # Draws 5 boxes of SolveNum Holder with DEFAULT values: 0 + 0 = 0 (MAYBE NO NEED IT HERE...)
            draw_solvenum_holder3(self.game_round_surface, (0, 0),
                                  solveNum_1, solveNum_Action, solveNum_2, solveNum_Result,
                                  blind, bonus_counter_progress)

            # Draws 0 - 9 Keyboard Holder and draws pressed button or mouse
            self.new_solution = draw_keyboard_holder_0_9(self.ui_surface, (0,0), (mx, my), key_pressed_num)

            # -------------------- Round STARTED and WAITING for answer from player -----------------#
            if self.is_round_timer_active:  # Calculate bonus timer for solvenumholder

                # -------------------------- NEW SOLVE TASK ROUND ----------------------#
                if self.generate_new_solve_task:  # creates new task to solve
                    solveNum_Action, solveNum_1, solveNum_2, solveNum_Result, blind, self.answer =\
                        create_solution_task3(self.level_id)
                    # --> run animation generating task
                    generate_solution_animation_counter += 1
                    is_bonus_counter_active = 0

                    if generate_solution_animation_counter == 20:  # if solution task is generated 40 times
                        self.generate_new_solve_task = 0  # --> #Set state to wait for answer mode
                        generate_solution_animation_counter = 0
                        bonus_started_timer = pygame.time.get_ticks()
                        is_bonus_counter_active = 1

                # Checking Bonus counter state, if active - iterate counter
                bonus_counter_progress, bonus_counter_value, is_bonus_counter_active =\
                    update_standard_counter_progress(bonus_started_timer, 5, is_bonus_counter_active, False)

                # Draws 5 boxes of SolveNum Holder with current solution task and updated bonus timer progress
                draw_solvenum_holder3(self.game_round_surface, (0, 0),
                                      solveNum_1, solveNum_Action, solveNum_2, solveNum_Result,
                                      blind, bonus_counter_progress)

                # CHECK FOR PLAYERS ANSWER
                # If No buttons pressed, pass and wait for pressed button
                if self.new_solution is None:
                    pass
                # SOLUTION CORRECT -> Adds to Round Score
                elif self.new_solution == self.answer:
                    self.player_current_round_score += 1 + is_bonus_counter_active * 2
                    react_on_answer(self.game_round_messages, 1, self.player_current_round_score)
                    self.game_round_messages_timer = 500
                    self.generate_new_solve_task = 1  # Set variables for new solution round

                # SOLUTION WRONG -> Deduct from Round Score
                else:
                    self.player_current_round_score -= 1
                    react_on_answer(self.game_round_messages, 0, self.player_current_round_score)
                    self.game_round_messages_timer = 500
                    self.generate_new_solve_task = 0

                self.new_solution = None

                # ROUND is running - > Update Round timer state
                self.round_timer_progress, self.round_timer_value, self.is_round_timer_active = \
                    update_standard_counter_progress(self.round_started_timer, 5*60, self.is_round_timer_active, False)

                # IF END OF THE ROUND (if round counter runs out...)
                if self.is_round_timer_active == 0:

                    react_on_round_end(self.display.screen, self.player_current_round_score)
                    # Saves Round Result to DB
                    db_add_round_result(self.player_id, self.level_id, self.player_current_round_score)
                    db_update_new_record(self.player_id, self.level_id, self.player_current_round_score)
                    # Reset Round Score to 0
                    self.player_current_round_score = 0

            # ROUND is not started (round timer was not started)
            else:
                # Display 100% timer on default
                self.round_timer_progress = 1

            # ------------------------------------- END OF FRAME procedures -------------------- #
            # Draw Surface to Monitor
            self.combine_all_game_layers()
            pygame.display.flip()

            # GAME TIMERS EXECUTION
            self.update_game_timers()  #ticks requested FPS and other timers...

            # Update window title
            pygame.display.set_caption(str(self.timer.get_fps()))

