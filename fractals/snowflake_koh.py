import turtle



def draw_kock_segment(t, ln):
    if ln > 6:
        ln3 = ln // 3
        draw_kock_segment(t, ln3)
        t.left(60)
        draw_kock_segment(t, ln3)
        t.right(120)
        draw_kock_segment(t, ln3)
        t.left(60)
        draw_kock_segment(t, ln3)
    else:
        t.fd(ln)
        t.left(60)
        t.fd(ln)
        t.right(120)
        t.fd(ln)
        t.left(60)
        t.fd(ln)


t = turtle.Turtle()
t.hideturtle()
t.speed(100)

draw_kock_segment(t, 150)
t.right(120)
draw_kock_segment(t, 150)
t.right(120)
draw_kock_segment(t, 150)


turtle.done()