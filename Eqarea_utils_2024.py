import numpy as np
import matplotlib.pylab as plt

#Funcoes para plot em equal area projection



def borda_proj(linestyle='-', c='k',linewidth=0.5):
    dec_proj = np.arange(0,361,1)
    inc_proj = np.zeros(361)
    DI = np.zeros([len(dec_proj),2])
    DI[:,0] = dec_proj 
    DI[:,1] = inc_proj 
    XYproj = dimap_eq(DI)
    plt.axis('equal')
    plt.axis('off')
    plt.text(-0.04,1.05,"N", fontsize=12)
    plt.text(-0.03,-1.12,"S", fontsize=12)
    plt.text(1.05,-0.03,"E", fontsize=12)
    plt.text(-1.15,-0.03,"W", fontsize=12)
    plt.plot([0,0],[1,1.03],linestyle=linestyle, c=c,linewidth=linewidth)
    plt.plot([0,0],[-1,-1.03],linestyle=linestyle, c=c,linewidth=linewidth)
    plt.plot([1,1.03],[0.,0.0],linestyle=linestyle, c=c,linewidth=linewidth)
    plt.plot([-1,-1.03],[0,0],linestyle=linestyle, c=c,linewidth=linewidth)
    plt.plot(XYproj[:,0],XYproj[:,1],linestyle=linestyle, c=c,linewidth=linewidth)

def circulo_inc(inc = 30, linestyle='--', c='k',linewidth=0.5):
    dec_proj = np.arange(0,361,1)
    inc_proj = np.ones(361)*inc
    DI = np.zeros([len(dec_proj),2])
    DI[:,0] = dec_proj 
    DI[:,1] = inc_proj 
    XYproj = dimap_eq(DI)
    plt.plot(XYproj[:,0],XYproj[:,1],linestyle=linestyle, c=c,linewidth=linewidth)
    
def marcadores_dec(intervalo, linestyle='-', c='k',linewidth=0.5):
    nmarcadores = int(360/intervalo) + 1
    for i in range(nmarcadores):
        Decmarc = np.array([i*intervalo,i*intervalo])
        incmarc = np.array([0,2])
        DI = np.zeros([len(Decmarc),2])
        DI[:,0] = Decmarc
        DI[:,1] =  incmarc 
        XYmarc = dimap_eq(DI)
        plt.plot(XYmarc[:,0], XYmarc[:,1],linestyle=linestyle, c=c,linewidth=linewidth)

def marcadores_inc(intervalo, linestyle='-', c='k',linewidth=0.5):
    nmarcadores = int(90/intervalo)
    for j in range(4):
        dec = 0.0 +j*90.
        for i in range(nmarcadores):
            Decmarc = np.array([dec,dec])
            incmarc = np.array([i*intervalo,i*intervalo])
            DI = np.zeros([len(Decmarc),2])
            DI[:,0] = Decmarc
            DI[:,1] =  incmarc 
            XYmarc = dimap_eq(DI)
            if dec==90. or dec ==270.:
                plt.plot(XYmarc[:,0], [-0.02,0.02],linestyle=linestyle, c=c,linewidth=linewidth)
            if dec==0. or dec ==180.:
                plt.plot([-0.02,0.02],XYmarc[:,1] ,linestyle=linestyle, c=c,linewidth=linewidth)

def grade(linestyle='-',c='k',linewidth=0.5):
    plt.plot([1,-1], [0,0], linestyle=linestyle,c=c,linewidth=linewidth)
    plt.plot([0,0], [1,-1], linestyle=linestyle,c=c,linewidth=linewidth)
def centro(linestyle='-', c='k',linewidth=0.5):
    plt.plot([-0.02,0.02],[0,0], linewidth=linewidth, c=c, linestyle=linestyle)
    plt.plot([0,0],[-0.02,0.02], linewidth=linewidth, c=c, linestyle=linestyle)

def proj_padrao():
    borda_proj()
    centro()
    marcadores_dec(10)
    marcadores_inc(10)
    centro()


  
def plot_dados(DI,nome='Dados direcionais', conectados = True, marker = 'o', markersize = 6,fillstyle='full', cormarcador = 'k',
               markeredgewidth=0.8, ls='-', linewidth=0.5,cordalinha='k', legenda=True, projecaopadrao = True):
    """Recebe uma matriz de duas colunas: Dec e Inc para plotar"""
    if projecaopadrao==True:
        proj_padrao()
    
    cor_interior_incpos=cormarcador
    cor_borda_incpos=cormarcador 
    cor_borda_incneg=cormarcador
    cor_interior_incneg='w'
    
    
    XYpoints = dimap_eq(DI)
    if conectados== True:
        plt.plot(XYpoints[:,0],XYpoints[:,1],ls=ls,linewidth=linewidth,color=cordalinha) 

    for i in range(len(XYpoints)):
        label = nome
        nome = ''
        if DI[i,1]<0.:
            plt.plot(XYpoints[i,0],XYpoints[i,1],marker = marker, markersize=markersize,fillstyle=fillstyle,
                     markeredgewidth=markeredgewidth, markerfacecolor=cor_interior_incneg,
                     markeredgecolor=cor_borda_incneg, ls='', label = label)
        else:
            plt.plot(XYpoints[i,0],XYpoints[i,1],marker = marker, markersize=markersize,fillstyle=fillstyle,
                     markeredgewidth=markeredgewidth, markerfacecolor=cor_interior_incpos,
                     markeredgecolor=cor_borda_incpos, ls='', label = label)
    if legenda==True:
        plt.legend()
					 
def plot_1dado(dec,inc, label='', marker = 'o', markersize = 6,fillstyle='full',
            markeredgewidth=0.8,cormarcador = 'k',projecaopadrao=True ):
    cor_interior_incpos=cormarcador
    cor_borda_incpos=cormarcador
    cor_interior_incneg='w'
    cor_borda_incneg=cormarcador

    if projecaopadrao==True:
        proj_padrao()

    DI = np.array(dec,inc)

    XYpoints = dimap_eq(DI)

    if inc<0.:
        plt.plot(XYpoints[0],XYpoints[1],marker = marker, markersize=markersize,fillstyle=fillstyle,
                     markeredgewidth=markeredgewidth, markerfacecolor=cor_interior_incneg,
                     markeredgecolor=cor_borda_incneg, ls='', label = label)
    else:
        plt.plot(XYpoints[0],XYpoints[1],marker = marker, markersize=markersize,fillstyle=fillstyle,
                     markeredgewidth=markeredgewidth, markerfacecolor=cor_interior_incpos,
                     markeredgecolor=cor_borda_incpos, ls='', label = label)

    
def dii2xyz(DII):
    """A entrada pode ser uma matriz de 3 ou 2 colunas:
     
    com 2 colunas: 
    declinação DII[:,0] e inclinação DII[:,1] 
    
    Com 3 colunas:
    declinação DII[:,0], inclinação DII[:,1] e intensidade [:,2]
    
    Os ângulos declinação e inclinação são dados em graus.
    Declinação é positiva no sentido horário e Inclinação é positiva para baixo.
    
    Retorno:
    
    A função retorna uma matriz com três colunas X(XYZ[:,0]), Y(XYZ[:,1]), Z(XYZ[:,2])"""
    
    XYZ = np.zeros([len(DII),3])
    
    if np.shape(DII)[1] == 2:
        XYZ[:,0] = np.cos(np.deg2rad(DII[:,0]))*np.cos(np.deg2rad(DII[:,1]))
        XYZ[:,1] = np.sin(np.deg2rad(DII[:,0]))*np.cos(np.deg2rad(DII[:,1]))
        XYZ[:,2] = np.sin(np.deg2rad(DII[:,1]))
    else:
        XYZ[:,0] = DII[:,2]*np.cos(np.deg2rad(DII[:,0]))*np.cos(np.deg2rad(DII[:,1]))
        XYZ[:,1] = DII[:,2]*np.sin(np.deg2rad(DII[:,0]))*np.cos(np.deg2rad(DII[:,1]))
        XYZ[:,2] = DII[:,2]*np.sin(np.deg2rad(DII[:,1]))

    return XYZ

def xyz2xyeq(XYZ):
    
    """A entrada é uma matriz de 3 colunas: X, Y e Z     
    Retorno:    
    A função retorna uma matriz com 3 colunas XYeq que são as coordenadas x e y da projeção estereografica
    A terceira coluna tem valor +1 para z >= 0"""
    
    XYZu = np.zeros_like(XYZ)

    XYZu[:,0] = XYZ[:,0]/np.sqrt((XYZ[:,0]**2)+(XYZ[:,1]**2)+(XYZ[:,2]**2))
    XYZu[:,1] = XYZ[:,1]/np.sqrt((XYZ[:,0]**2)+(XYZ[:,1]**2)+(XYZ[:,2]**2))
    XYZu[:,2] = XYZ[:,2]/np.sqrt((XYZ[:,0]**2)+(XYZ[:,1]**2)+(XYZ[:,2]**2))

    XYeq = np.zeros([len(XYZ),3])
    
    for i in range(len(XYZu)):
        
        if XYZu[i,2] != 1.:
            # Collinson 1983 pagina 361 R = Ro(1-raiz(1-sen(inclinacao))) para projeção equal-area
            # usaremos um círculo de raio 1, Ro  = 1
            # R é a medida da borda do circulo até o ponto que queremos projetar
            # Sendo R = 1*(1 - a), vou pegar a para calcular o ponto x e y da projeção
            # a = raiz(1-sen(inclinacao))
            # xeq = Yu*a/cos(Inclinacao) yeq = Yu*a/cos(Inclinacao)
            # b = a/cosI = raiz(1-Zu)/raiz(xˆ2+yˆ2)
            
            b = np.sqrt(1-np.abs(XYZu[i,2]))/np.sqrt(XYZu[i,0]**2 +XYZu[i,1]**2)
            XYeq[i,0] =  b * XYZu[i,1]
            XYeq[i,1] =  b * XYZu[i,0]
            
        if XYZu[i,2] >= 0.:
            #apenas para uso do plot (+1 símbolo cheio)
            XYeq[i,2] = 1.
        else:
            XYeq[i,2] = -1.
            
    return XYeq

def dimap_eq(DII):
    """A entrada pode ser uma matriz de 3 ou 2 colunas:
     
    com 2 colunas: 
    declinação DII[:,0] e inclinação DII[:,1] 
    
    Com 3 colunas:
    declinação DII[:,0], inclinação DII[:,1] e intensidade [:,2]
    
    Os ângulos declinação e inclinação são dados em graus.
    Declinação é positiva no sentido horário e Inclinação é positiva para baixo.
    
    Retorno:
    
    A função retorna as coordenadas XY da projeção equal area com três colunas Xeq, Yeq, 
    terceira coluna é +1 para inc positiva e -1 para inc negativa"""
    XYZ = dii2xyz(DII[:,0:2])
    XYeq = xyz2xyeq(XYZ)
    
    return XYeq