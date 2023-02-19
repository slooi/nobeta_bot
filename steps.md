# SETUP

-   Position character so you can hit then with fireball when they spawn

# CODE HIGH LEVEL

1. Every 0.2 secs, check if a bunch of pixels are black (enemy spawned) around the center of screen
2. When enemy detected shoot
3. Wait 0.2 secs then recharge
4. Wait 1 sec then hold 'w' key
5. Keep walking forwards until a bunch of pixels are purple around the center of screen
6. go back to 1.

# CODE FUNCTIONS

## MAIN (DETECTION)

1. Detect if enemy spawned (enemy_has_spawned)
2. Detect if at shooting position (is_at_shooting_position)

## MINOR (ACTION)

3. Move back to shooting position (move_to_shooting_position)
4. shoot
5. reload
6. wait

# How to do 1. and 2.

## 1 Detect if enemy spawned (enemy_has_spawned)

-   Check if a certain AREA of screen (horizontal center) contain at least 15/20 black pixels (3/255,3/255,3/255 and lower)
-   This kernal should be FALSE everywhere else in that horizontal center area

## 2 Detect if at shooting position (is_at_shooting_position)

-   Check if a certain AREA of screen (right-center ish area) contain at least 10/100 of pixels with purple
-   This kernel should be FALSE every where else in image

# Worries

1. Performance of pixel checks
2. Latency between detection and action (mob detected and shooting)
3.

# NOTES

## Area of circle

997,557
1248,671

## Area of spawn particles

741,141
1144,135
