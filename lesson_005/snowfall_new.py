import simple_draw as sd
sd.resolution = (1200, 600)

def snow():
    x = sd.random_number(0, 1100)
    y = 600


    length = sd.random_number(20, 70)
    f_a = sd.random_number(2, 8) / 10
    f_b = sd.random_number(20, 70) / 100
    f_c = sd.random_number(30, 75)


    while True:


        sd.snowflake(center=sd.get_point(x, y), length=length, factor_a=f_a, factor_b=f_b, factor_c=f_c)
        pass
        pass
        sd.sleep(0.1)
        sd.snowflake(center=sd.get_point(x, y), length=length, color=sd.background_color,
                     factor_a=f_a, factor_b=f_b, factor_c=f_c)
        y -= 50

        if y < length:
            sd.snowflake(center=sd.get_point(x, y), length=length, factor_a=f_a, factor_b=f_b, factor_c=f_c)
            y = 600
            x = sd.random_number(0, 1100)
            snow()
        if sd.user_want_exit():
            break

snow()



sd.pause()