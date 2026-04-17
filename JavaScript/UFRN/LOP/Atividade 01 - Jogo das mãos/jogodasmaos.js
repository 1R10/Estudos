var tela = 0;
var doce = '';
var doce2 = '';
function setup() {
  createCanvas(400, 400);
}

function draw() {
  if (tela==0){ //menu
  background('darkblue');
  fill("rgb(48,208,48)");
  (rect(100,100, 200, 50));//posx,posy, larg, alt
  textSize(20);
  fill(255);
  text('Jogo', 175, 133);

  fill("rgb(48,208,48)");//bot de instr.
  (rect(100,200, 200, 50));
  textSize(20);
  fill(255);
  text('Instruções', 155, 233);
  doce  = ''
  doce2 = ''

  print('X:', mouseX,'nY:' , mouseY)
  }
  
  if (tela==1){// p1
    background(220);
    textSize(30)
    fill('black')
    text('Jogador 1',120,60)
    textSize(15)
    text('Escolha em qual mão o doce ficará escondido:',45,90)
    fill("darkblue");
    rect(100, 190, 200, 50);
    textSize(20);
    fill(255);
    text('Esquerda', 160, 225);
    fill("black");
    rect(100, 250, 200, 50);
    textSize(20);
    fill(255);
    text('Direita', 170, 285);
    rect(380, 10, 10, 10)
    textSize(8)
    fill('black')
    text('X', 382, 18)  // voltar   
    print('X:', mouseX,'nY:' , mouseY)
}
    if (tela==11){//p1 vitoria
        background('darkblue')
        fill('white')
        rect(60, 30, 280, 275)
        textSize(15)
        fill('black')
        text('VITÓRIA DO JOGADOR N°1!', 100, 70)
        fill('black')
        text('O doce estava na mão ' + doce, 70, 100)
        fill(225)
        rect(380, 10, 10, 10)
        textSize(8)
        fill('black')
        text('X', 382, 18)
        
    } 

    if (tela==2){//p2
    background(220);
    textSize(30)
    fill('black')
    text('Jogador 2',120,60)
    textSize(15)
    text('Advinhe em qual mão o doce foi escondido:',55,90)
    fill("darkblue");
    rect(100, 190, 200, 50);
    textSize(20);
    fill(255);
    text('Esquerda', 160, 225);
    fill("black");
    rect(100, 250, 200, 50);
    textSize(20);
    fill(255);
    text('Direita', 170, 285);
    
    }
    if (tela==22){//p2 vitoria
    background('darkblue')
    fill('white')
    rect(60, 30, 280, 275)
    textSize(15)
    fill('black')
    text('VITÓRIA DO JOGADOR N°2!', 100, 70)
    fill('black')
    text('O doce estava na mão ' + doce, 70, 100)
    fill(225)
    rect(380, 10, 10, 10)
    textSize(8)
    fill('black')
    text('X', 382, 18)        
    } 

    if (tela==9){
    background(220);
    fill("black");
    rect(60, 30, 280, 275);
    textSize(20);
    fill(255);
    text('Instruções', 150, 60);
    textSize(10)
    text('Jogador 1 precisa guardar a bala em uma mão;',80, 100);
    text('Escolha em qual mão escolher clicando no botão;',80, 115)
    text('Jogador 2 precisa advinhar a mão que está a bala;',80, 130);
    text('Escolha em qual mão escolher clicando no botão.',80, 145);  
    text('Clique na tela para voltar ao menu.',80, 290);    
    textSize(20)
    text('Divirta-se!!!',80,270)
  
    print('X:', mouseX,'nY:' , mouseY);
    }
}

function mouseClicked(){
    print(tela)

if(tela==0){// menu
    if (mouseX > 100 && mouseX < 300 && mouseY > 100 && mouseY < 150){
    tela = 1;
}
    else if (mouseX > 100 && mouseX < 300 && mouseY > 200 && mouseY < 250){
    tela = 9;
    }

}

else if (tela==1){// p1
    if (mouseX > 380 && mouseX < 390 && mouseY > 10 && mouseY < 20){
    tela = 0;
}
    if (mouseX > 100 && mouseX < 300 && mouseY > 190 && mouseY < 240){
        doce = 'esquerda'
        print(doce)
        tela = 2; 
    }
    if  (mouseX > 100 && mouseX < 300 && mouseY > 250 && mouseY < 300){
        doce = 'direita'
        print(doce)
        tela = 2; 
    }
}
else if (tela==2){// p2
        if (mouseX > 100 && mouseX < 300 && mouseY > 190 && mouseY < 240){
        doce2 = 'esquerda';
        print(doce2); 
        if (doce == doce2){
            tela=22
        }
        else if (doce != doce2){
            tela = 11
        }else{
            tela =22
        }

    }
    if  (mouseX > 100 && mouseX < 300 && mouseY > 250 && mouseY < 300){
        doce2 = 'direita';
        print(doce2);
        if (doce == doce2){
            tela = 22
        }
        else {
            tela = 11
        }
         
    }
}
else if (tela == 11 || tela == 22){
    if (mouseX > 380 && mouseX < 390 && mouseY > 10 && mouseY < 20){
    tela = 0;
}
}
else if (tela==9){// instruções
    tela = 0
}

}