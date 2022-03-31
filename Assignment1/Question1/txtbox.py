# Utiity function for printing textbox in plots

def txtbox(plt, alpha, A, omega):

    # box content
    textstr = '\n'.join((
        r'$\alpha=%.1f$' % (alpha, ),
        r'$\mathrm{A}=%.1f$' % (A, ),
        r'$\omega=%.1f$' % (omega, ))
    )

    # draw the textbox
    plt.text(
        0.75, 
        0.7, 
        textstr, 
        fontsize=12, 
        bbox = dict(facecolor = 'blue', alpha = 0.3)
    )

    return plt