package A13514;
import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.ArrayList;

interface Figure{
    void draw(Graphics g);
}

class Rect implements Figure{
    private final int x1;
    private final int y1;
    private final int x2;
    private final int y2;

    public Rect(int x1, int y1, int x2, int y2) {
        this.x1 = x1;
        this.x2 = x2;
        this.y1 = y1;
        this.y2 = y2;
    }
    @Override
    public void draw(Graphics g) {
        if(this.x1<this.x2) {
            if (this.y1 < this.y2)
                g.drawRect(this.x1, this.y1, this.x2 - this.x1, this.y2 - this.y1);
            else
                g.drawRect(this.x1, this.y2, this.x2 - this.x1,this.y1-this.y2);
        }else{
            if (this.y1 > this.y2)
                g.drawRect(this.x2, this.y2, this.x1 - this.x2, this.y1 - this.y2);
            else
                g.drawRect(this.x2, this.y1, this.x1 - this.x2,this.y2-this.y1);
        }
    }
}

class Oval implements Figure{
    private final int x1;
    private final int y1;
    private final int x2;
    private final int y2;

    public Oval(int x1, int y1, int x2, int y2) {
        this.x1 = x1;
        this.x2 = x2;
        this.y1 = y1;
        this.y2 = y2;
    }
    @Override
    public void draw(Graphics g) {
        if(this.x1<this.x2) {
            if (this.y1 < this.y2)
                g.drawOval(this.x1, this.y1, this.x2 - this.x1, this.y2 - this.y1);
            else
                g.drawOval(this.x1, this.y2, this.x2 - this.x1,this.y1-this.y2);
        }else{
            if (this.y1 > this.y2)
                g.drawOval(this.x2, this.y2, this.x1 - this.x2, this.y1 - this.y2);
            else
                g.drawOval(this.x2, this.y1, this.x1 - this.x2,this.y2-this.y1);
        }
    }
}

class Line implements Figure{
    private final int x1;
    private final int y1;
    private final int x2;
    private final int y2;

    public Line(int x1, int y1, int x2, int y2) {
        this.x1 = x1;
        this.x2 = x2;
        this.y1 = y1;
        this.y2 = y2;
    }
    @Override
    public void draw(Graphics g) {
        g.drawLine(this.x1,this.y1,this.x2,this.y2);
    }
}
class MyPanel extends JPanel{
    private final ArrayList<Figure> figures;
    public MyPanel(){
        this.figures=new ArrayList<>();
        setBackground(Color.white);
        addMouseListener(new MyListenner());
        Font font=new Font("궁서",Font.BOLD,20);
        this.setFont(font);
    }
    @Override
    public void paint(Graphics g){
        super.paint(g);
        g.setColor(Color.red);
        g.drawRect(125,0,100,50);
        g.drawRect(325,0,100,50);
        g.drawRect(525,0,100,50);
        g.setColor(Color.black);
        g.drawString("사각형",150,30);
        g.drawString("원형",360,30);
        g.drawString("선분",560,30);
        for(Figure s:this.figures){
            s.draw(g);
        }
    }

    class MyListenner implements MouseListener {
        private int x1;
        private int y1;
        private int x2;
        private int y2;
        private int flag=-1;
        @Override
        public void mouseClicked(MouseEvent e) {
        }

        @Override
        public void mousePressed(MouseEvent e) {
            this.x1=e.getX();
            this.y1=e.getY();
        }

        @Override
        public void mouseReleased(MouseEvent e) {
            this.x2=e.getX();
            this.y2=e.getY();
            if((this.x1>=125&&this.x1<=225)&&(this.y1>=0&&this.y1<=50)){
                flag=0;
            }else if((this.x1>=325&&this.x1<=425)&&(this.y1>=0&&this.y1<=50)){
                flag=1;
            }else if((this.x1>=525&&this.x1<=625)&&(this.y1>=0&&this.y1<=50)){
                flag=2;
            }else if(flag==0){
                add(new Rect(this.x1,this.y1,this.x2,this.y2));
                flag=-1;
            }else if(flag==1){
                add(new Oval(this.x1,this.y1,this.x2,this.y2));
                flag=-1;
            }else if(flag==2){
                add(new Line(this.x1,this.y1,this.x2,this.y2));
                flag=-1;
            }

        }

        @Override
        public void mouseEntered(MouseEvent e) {

        }

        @Override
        public void mouseExited(MouseEvent e) {

        }
        public void add(Figure figure){
            figures.add(figure);
            repaint();
        }

    }
}

class MyFrame extends JFrame {
    public MyFrame(){
    }
}

public class Main {
    public static void main(String[] args) {
        JFrame frame=new JFrame();

        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.setContentPane(new MyPanel());
        frame.setSize(750,500);
        frame.setVisible(true);
    }
}
