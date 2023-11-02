/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JInternalFrame.java to edit this template
 */
package vista;

import controlador.controladorFarmacia;
import java.awt.Image;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.Iterator;
import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.table.DefaultTableModel;
import modelo.Farmacia;
import static vista.Index.panelSecundario;
import static vista.Registro.unAreaADM;

/**
 *
 * @author ADMON
 */
public class DatosFarmacia extends javax.swing.JInternalFrame {

//  controlador para llamar el swich de opciones del crud

    controladorFarmacia controlarFarmacia = new controladorFarmacia();
    DefaultTableModel tabla;   
    
    
    public DatosFarmacia() {
        initComponents();
        cargarMetodos();
        
    
    }
    
    private void cargarMetodos (){
        
        agregarImgs();
        funcionesExtras();
        llenarTabla();
    
    
    };
    
    private void agregarImgs(){
        
        // icono del edificio a la izquierda 
    
       ImageIcon importarIconoF = (new ImageIcon("imgs/edificio.png"));
       JLabel edificioImg =new JLabel();
       edificioImg.setIcon(new ImageIcon(importarIconoF.getImage().getScaledInstance(33,45, Image.SCALE_SMOOTH)));
       edificioImg.setBounds(118,41,33,45);
       panelFarmacia.add(edificioImg);
       
       // icono del logo abajo 
       ImageIcon importarIcono2 = (new ImageIcon("imgs/logoQ1.png"));
       JLabel logoF =new JLabel();
       logoF.setIcon(new ImageIcon(importarIcono2.getImage().getScaledInstance(36,36, Image.SCALE_SMOOTH)));
       logoF.setBounds(713,725,36,36);
       panelFarmacia.add(logoF);   
       
       // icono de la flecha a la izquierda
       ImageIcon importarFlecha = (new ImageIcon("imgs/flechaIzq.png"));
       JLabel iconoFlecha = new JLabel();
       iconoFlecha.setIcon(new ImageIcon(importarFlecha.getImage().getScaledInstance(33,33, Image.SCALE_SMOOTH)));
       iconoFlecha.setBounds(20,25,33,33);
       iconoFlecha.setCursor( new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR){});// curso de la mano 
       panelFarmacia.add(iconoFlecha);  
       
        //eventos de escucha de la imagen registro 
       
        int cont = 0 ;
       
            iconoFlecha.addMouseListener(new MouseAdapter() {
            
            @Override
            public void mouseClicked(MouseEvent e) {   
              retornarAreaAdministracion();    
            }
            }
            );
    }
    
    private void funcionesExtras(){
        
       this.setBounds(40, 10, this.getWidth(), this.getHeight());
       spinnerId.setVisible(false);// cambiar 
       btnModificar.setEnabled(false);
       btnEliminar.setEnabled(false);
       
    }
    
    private void retornarAreaAdministracion(){
        this.setVisible(false);
        unAreaADM.setVisible(true);
    }
    
    // este caso se esta mostrando los mismos datos que el usurio ingresa entonces por decir los datos van a los getter llegando asignarselos en alguna parte en
    // este parte el id no le esta asignando a nada porque esta excluido de la tabla , creo que si o si se tendria que guardar ese dato en la tabla o la otra es 
    // una consulta para id y listo o ves de eliminar con el id en la tabla e farmacia seria eliminar con el nit aunque esta sirvira porque el nit es unico pero
    // en otras tablas no esta por lo tanto mirar que hacer..
            
            

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jButton1 = new javax.swing.JButton();
        jPopupMenu1 = new javax.swing.JPopupMenu();
        jRadioButtonMenuItem1 = new javax.swing.JRadioButtonMenuItem();
        panelFarmacia = new javax.swing.JPanel();
        vSuperOfertas = new javax.swing.JLabel();
        jSeparator1 = new javax.swing.JSeparator();
        jLabel6 = new javax.swing.JLabel();
        txtNitFarmacia = new javax.swing.JTextField();
        jLabel10 = new javax.swing.JLabel();
        txtNombreFarmacia = new javax.swing.JTextField();
        jLabel7 = new javax.swing.JLabel();
        txtTelefonoFarmacia = new javax.swing.JTextField();
        jLabel8 = new javax.swing.JLabel();
        txtCorreoFarmacia = new javax.swing.JTextField();
        jLabel9 = new javax.swing.JLabel();
        txtUbicacionFarmacia = new javax.swing.JTextField();
        btnIngresar = new javax.swing.JButton();
        btnLimpiar = new javax.swing.JButton();
        btnEliminar = new javax.swing.JButton();
        btnModificar = new javax.swing.JButton();
        jLabel11 = new javax.swing.JLabel();
        labelFarmacit = new javax.swing.JLabel();
        jSeparator4 = new javax.swing.JSeparator();
        jSeparator5 = new javax.swing.JSeparator();
        txtBuscar = new javax.swing.JTextField();
        spinnerId = new javax.swing.JSpinner();
        btnBuscar = new javax.swing.JButton();
        jScrollPane2 = new javax.swing.JScrollPane();
        tablaDatosFarmacia = new javax.swing.JTable();

        jButton1.setText("jButton1");

        jRadioButtonMenuItem1.setSelected(true);
        jRadioButtonMenuItem1.setText("jRadioButtonMenuItem1");

        setBackground(new java.awt.Color(255, 255, 249));
        setClosable(true);
        addInternalFrameListener(new javax.swing.event.InternalFrameListener() {
            public void internalFrameActivated(javax.swing.event.InternalFrameEvent evt) {
            }
            public void internalFrameClosed(javax.swing.event.InternalFrameEvent evt) {
                formInternalFrameClosed(evt);
            }
            public void internalFrameClosing(javax.swing.event.InternalFrameEvent evt) {
            }
            public void internalFrameDeactivated(javax.swing.event.InternalFrameEvent evt) {
            }
            public void internalFrameDeiconified(javax.swing.event.InternalFrameEvent evt) {
            }
            public void internalFrameIconified(javax.swing.event.InternalFrameEvent evt) {
            }
            public void internalFrameOpened(javax.swing.event.InternalFrameEvent evt) {
            }
        });

        panelFarmacia.setBackground(new java.awt.Color(255, 255, 255));

        vSuperOfertas.setFont(new java.awt.Font("PT Sans Narrow", 0, 35)); // NOI18N
        vSuperOfertas.setText("Farmacias");
        vSuperOfertas.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        vSuperOfertas.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseEntered(java.awt.event.MouseEvent evt) {
                vSuperOfertasMouseEntered(evt);
            }
            public void mouseExited(java.awt.event.MouseEvent evt) {
                vSuperOfertasMouseExited(evt);
            }
        });

        jSeparator1.setForeground(new java.awt.Color(0, 0, 0));

        jLabel6.setFont(new java.awt.Font("PT Sans Narrow", 0, 22)); // NOI18N
        jLabel6.setText("nitFarmacia");

        txtNitFarmacia.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        txtNitFarmacia.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                txtNitFarmaciaActionPerformed(evt);
            }
        });

        jLabel10.setFont(new java.awt.Font("PT Sans Narrow", 0, 22)); // NOI18N
        jLabel10.setText("nombreFarmacia");

        txtNombreFarmacia.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        txtNombreFarmacia.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                txtNombreFarmaciaActionPerformed(evt);
            }
        });

        jLabel7.setFont(new java.awt.Font("PT Sans Narrow", 0, 22)); // NOI18N
        jLabel7.setText("telefonoFarmacia");

        txtTelefonoFarmacia.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        txtTelefonoFarmacia.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                txtTelefonoFarmaciaActionPerformed(evt);
            }
        });

        jLabel8.setFont(new java.awt.Font("PT Sans Narrow", 0, 22)); // NOI18N
        jLabel8.setText("correoFarmacia");

        txtCorreoFarmacia.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        txtCorreoFarmacia.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                txtCorreoFarmaciaActionPerformed(evt);
            }
        });

        jLabel9.setFont(new java.awt.Font("PT Sans Narrow", 0, 22)); // NOI18N
        jLabel9.setText("ubicacionFarmacia");

        txtUbicacionFarmacia.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        txtUbicacionFarmacia.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                txtUbicacionFarmaciaActionPerformed(evt);
            }
        });

        btnIngresar.setBackground(new java.awt.Color(0, 102, 255));
        btnIngresar.setFont(new java.awt.Font("PT Sans Narrow", 0, 18)); // NOI18N
        btnIngresar.setText("Insertar");
        btnIngresar.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        btnIngresar.setName("Insertar"); // NOI18N
        btnIngresar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnIngresarActionPerformed(evt);
            }
        });

        btnLimpiar.setBackground(new java.awt.Color(0, 102, 255));
        btnLimpiar.setFont(new java.awt.Font("PT Sans Narrow", 0, 18)); // NOI18N
        btnLimpiar.setText("Limpiar");
        btnLimpiar.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        btnLimpiar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnLimpiarActionPerformed(evt);
            }
        });

        btnEliminar.setBackground(new java.awt.Color(0, 102, 255));
        btnEliminar.setFont(new java.awt.Font("PT Sans Narrow", 0, 18)); // NOI18N
        btnEliminar.setText("Eliminar");
        btnEliminar.setToolTipText("");
        btnEliminar.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        btnEliminar.setName("Eliminar"); // NOI18N
        btnEliminar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnEliminarActionPerformed(evt);
            }
        });

        btnModificar.setBackground(new java.awt.Color(0, 102, 255));
        btnModificar.setFont(new java.awt.Font("PT Sans Narrow", 0, 18)); // NOI18N
        btnModificar.setText("Modificar");
        btnModificar.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        btnModificar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnModificarActionPerformed(evt);
            }
        });

        jLabel11.setFont(new java.awt.Font("PT Sans Narrow", 0, 24)); // NOI18N
        jLabel11.setText("Ingresar una farmacia");

        labelFarmacit.setFont(new java.awt.Font("PT Sans Narrow", 0, 35)); // NOI18N
        labelFarmacit.setText("Farmacit");
        labelFarmacit.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        labelFarmacit.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseEntered(java.awt.event.MouseEvent evt) {
                labelFarmacitMouseEntered(evt);
            }
            public void mouseExited(java.awt.event.MouseEvent evt) {
                labelFarmacitMouseExited(evt);
            }
        });

        jSeparator4.setForeground(new java.awt.Color(0, 0, 0));

        jSeparator5.setForeground(new java.awt.Color(0, 0, 0));

        txtBuscar.setFont(new java.awt.Font("PT Sans Narrow", 0, 18)); // NOI18N
        txtBuscar.setText("  Buscar una farmacia");
        txtBuscar.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));

        spinnerId.setEnabled(false);

        btnBuscar.setText("buscar");
        btnBuscar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnBuscarActionPerformed(evt);
            }
        });

        tablaDatosFarmacia.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null, null, null, null, null},
                {null, null, null, null, null, null},
                {null, null, null, null, null, null},
                {null, null, null, null, null, null}
            },
            new String [] {
                "idFarmacia", "nitFarmacia", "nombreFarmacia", "telefonoFarmacia", "correoFarmacia", "ubicacionFarmacia"
            }
        ) {
            Class[] types = new Class [] {
                java.lang.Integer.class, java.lang.String.class, java.lang.String.class, java.lang.String.class, java.lang.String.class, java.lang.String.class
            };
            boolean[] canEdit = new boolean [] {
                false, false, false, false, false, false
            };

            public Class getColumnClass(int columnIndex) {
                return types [columnIndex];
            }

            public boolean isCellEditable(int rowIndex, int columnIndex) {
                return canEdit [columnIndex];
            }
        });
        tablaDatosFarmacia.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                tablaDatosFarmaciaMouseClicked(evt);
            }
        });
        jScrollPane2.setViewportView(tablaDatosFarmacia);

        javax.swing.GroupLayout panelFarmaciaLayout = new javax.swing.GroupLayout(panelFarmacia);
        panelFarmacia.setLayout(panelFarmaciaLayout);
        panelFarmaciaLayout.setHorizontalGroup(
            panelFarmaciaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, panelFarmaciaLayout.createSequentialGroup()
                .addGap(0, 0, Short.MAX_VALUE)
                .addGroup(panelFarmaciaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, panelFarmaciaLayout.createSequentialGroup()
                        .addComponent(jLabel11)
                        .addGap(636, 636, 636))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, panelFarmaciaLayout.createSequentialGroup()
                        .addComponent(labelFarmacit)
                        .addGap(641, 641, 641))))
            .addGroup(panelFarmaciaLayout.createSequentialGroup()
                .addGap(158, 158, 158)
                .addGroup(panelFarmaciaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(panelFarmaciaLayout.createSequentialGroup()
                        .addComponent(jScrollPane2, javax.swing.GroupLayout.PREFERRED_SIZE, 1174, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                    .addGroup(panelFarmaciaLayout.createSequentialGroup()
                        .addComponent(vSuperOfertas)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(txtBuscar, javax.swing.GroupLayout.PREFERRED_SIZE, 166, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(btnBuscar)
                        .addGap(192, 192, 192))))
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, panelFarmaciaLayout.createSequentialGroup()
                .addContainerGap(92, Short.MAX_VALUE)
                .addGroup(panelFarmaciaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(panelFarmaciaLayout.createSequentialGroup()
                        .addComponent(spinnerId, javax.swing.GroupLayout.PREFERRED_SIZE, 63, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(18, 18, 18)
                        .addGroup(panelFarmaciaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addGroup(panelFarmaciaLayout.createSequentialGroup()
                                .addComponent(txtNitFarmacia, javax.swing.GroupLayout.PREFERRED_SIZE, 177, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addGap(36, 36, 36)
                                .addComponent(txtNombreFarmacia, javax.swing.GroupLayout.PREFERRED_SIZE, 179, javax.swing.GroupLayout.PREFERRED_SIZE))
                            .addGroup(panelFarmaciaLayout.createSequentialGroup()
                                .addComponent(jLabel6)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                .addComponent(jLabel10)
                                .addGap(37, 37, 37)))
                        .addGroup(panelFarmaciaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(panelFarmaciaLayout.createSequentialGroup()
                                .addGap(46, 46, 46)
                                .addComponent(txtTelefonoFarmacia, javax.swing.GroupLayout.PREFERRED_SIZE, 171, javax.swing.GroupLayout.PREFERRED_SIZE))
                            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, panelFarmaciaLayout.createSequentialGroup()
                                .addComponent(jLabel7)
                                .addGap(24, 24, 24)))
                        .addGroup(panelFarmaciaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(panelFarmaciaLayout.createSequentialGroup()
                                .addGap(70, 70, 70)
                                .addComponent(jLabel8)
                                .addGap(83, 83, 83)
                                .addComponent(jLabel9))
                            .addGroup(panelFarmaciaLayout.createSequentialGroup()
                                .addGap(46, 46, 46)
                                .addComponent(txtCorreoFarmacia, javax.swing.GroupLayout.PREFERRED_SIZE, 171, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addGap(45, 45, 45)
                                .addComponent(txtUbicacionFarmacia, javax.swing.GroupLayout.PREFERRED_SIZE, 161, javax.swing.GroupLayout.PREFERRED_SIZE)))
                        .addGap(31, 31, 31)
                        .addGroup(panelFarmaciaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(panelFarmaciaLayout.createSequentialGroup()
                                .addComponent(btnModificar)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(btnLimpiar))
                            .addGroup(panelFarmaciaLayout.createSequentialGroup()
                                .addComponent(btnIngresar)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(btnEliminar)))
                        .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, panelFarmaciaLayout.createSequentialGroup()
                        .addComponent(jSeparator1, javax.swing.GroupLayout.PREFERRED_SIZE, 1367, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(42, 42, 42))))
            .addGroup(panelFarmaciaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, panelFarmaciaLayout.createSequentialGroup()
                    .addContainerGap(79, Short.MAX_VALUE)
                    .addComponent(jSeparator4, javax.swing.GroupLayout.PREFERRED_SIZE, 1367, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addGap(55, 55, 55)))
            .addGroup(panelFarmaciaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, panelFarmaciaLayout.createSequentialGroup()
                    .addContainerGap(88, Short.MAX_VALUE)
                    .addComponent(jSeparator5, javax.swing.GroupLayout.PREFERRED_SIZE, 1367, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addGap(46, 46, 46)))
        );
        panelFarmaciaLayout.setVerticalGroup(
            panelFarmaciaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(panelFarmaciaLayout.createSequentialGroup()
                .addGap(46, 46, 46)
                .addGroup(panelFarmaciaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addComponent(vSuperOfertas, javax.swing.GroupLayout.PREFERRED_SIZE, 25, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addGroup(panelFarmaciaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                        .addComponent(txtBuscar, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addComponent(btnBuscar)))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 63, Short.MAX_VALUE)
                .addComponent(jScrollPane2, javax.swing.GroupLayout.PREFERRED_SIZE, 359, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(33, 33, 33)
                .addComponent(jLabel11, javax.swing.GroupLayout.PREFERRED_SIZE, 28, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGroup(panelFarmaciaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(panelFarmaciaLayout.createSequentialGroup()
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 42, Short.MAX_VALUE)
                        .addGroup(panelFarmaciaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(btnIngresar)
                            .addComponent(btnEliminar))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(panelFarmaciaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(btnModificar)
                            .addComponent(btnLimpiar))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED))
                    .addGroup(panelFarmaciaLayout.createSequentialGroup()
                        .addGap(36, 36, 36)
                        .addGroup(panelFarmaciaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addGroup(panelFarmaciaLayout.createSequentialGroup()
                                .addComponent(jLabel10, javax.swing.GroupLayout.PREFERRED_SIZE, 28, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(txtNombreFarmacia, javax.swing.GroupLayout.PREFERRED_SIZE, 32, javax.swing.GroupLayout.PREFERRED_SIZE))
                            .addGroup(panelFarmaciaLayout.createSequentialGroup()
                                .addGroup(panelFarmaciaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                    .addComponent(jLabel8, javax.swing.GroupLayout.PREFERRED_SIZE, 28, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jLabel9, javax.swing.GroupLayout.PREFERRED_SIZE, 28, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jLabel7, javax.swing.GroupLayout.PREFERRED_SIZE, 28, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(panelFarmaciaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(txtTelefonoFarmacia, javax.swing.GroupLayout.PREFERRED_SIZE, 32, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addGroup(panelFarmaciaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                        .addComponent(txtUbicacionFarmacia, javax.swing.GroupLayout.PREFERRED_SIZE, 32, javax.swing.GroupLayout.PREFERRED_SIZE)
                                        .addComponent(txtCorreoFarmacia, javax.swing.GroupLayout.PREFERRED_SIZE, 32, javax.swing.GroupLayout.PREFERRED_SIZE))))
                            .addGroup(panelFarmaciaLayout.createSequentialGroup()
                                .addComponent(jLabel6, javax.swing.GroupLayout.PREFERRED_SIZE, 28, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(panelFarmaciaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                    .addComponent(txtNitFarmacia, javax.swing.GroupLayout.PREFERRED_SIZE, 32, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(spinnerId, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))))
                        .addGap(19, 19, 19)))
                .addComponent(jSeparator1, javax.swing.GroupLayout.PREFERRED_SIZE, 19, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(labelFarmacit, javax.swing.GroupLayout.PREFERRED_SIZE, 40, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18))
            .addGroup(panelFarmaciaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                .addGroup(panelFarmaciaLayout.createSequentialGroup()
                    .addGap(92, 92, 92)
                    .addComponent(jSeparator4, javax.swing.GroupLayout.PREFERRED_SIZE, 19, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addContainerGap(636, Short.MAX_VALUE)))
            .addGroup(panelFarmaciaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, panelFarmaciaLayout.createSequentialGroup()
                    .addContainerGap(558, Short.MAX_VALUE)
                    .addComponent(jSeparator5, javax.swing.GroupLayout.PREFERRED_SIZE, 19, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addGap(170, 170, 170)))
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addComponent(panelFarmacia, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(0, 0, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addComponent(panelFarmacia, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(0, 0, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void txtUbicacionFarmaciaActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_txtUbicacionFarmaciaActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_txtUbicacionFarmaciaActionPerformed

    private void txtCorreoFarmaciaActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_txtCorreoFarmaciaActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_txtCorreoFarmaciaActionPerformed

    private void txtTelefonoFarmaciaActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_txtTelefonoFarmaciaActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_txtTelefonoFarmaciaActionPerformed

    private void txtNombreFarmaciaActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_txtNombreFarmaciaActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_txtNombreFarmaciaActionPerformed

    private void txtNitFarmaciaActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_txtNitFarmaciaActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_txtNitFarmaciaActionPerformed

    private void vSuperOfertasMouseExited(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_vSuperOfertasMouseExited
        // TODO add your handling code here:
    }//GEN-LAST:event_vSuperOfertasMouseExited

    private void vSuperOfertasMouseEntered(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_vSuperOfertasMouseEntered
        // TODO add your handling code here:
    }//GEN-LAST:event_vSuperOfertasMouseEntered

    private void btnModificarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnModificarActionPerformed
      controlarFarmacia.controlarAccion(evt, obtenerFarmacia());
      limpiarDatosFarmacia();
      tabla.setRowCount(0);
      llenarTabla();
    }//GEN-LAST:event_btnModificarActionPerformed

    private void labelFarmacitMouseEntered(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_labelFarmacitMouseEntered
        // TODO add your handling code here:

    }//GEN-LAST:event_labelFarmacitMouseEntered

    private void labelFarmacitMouseExited(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_labelFarmacitMouseExited
        // TODO add your handling code here:
    }//GEN-LAST:event_labelFarmacitMouseExited

    private void formInternalFrameClosed(javax.swing.event.InternalFrameEvent evt) {//GEN-FIRST:event_formInternalFrameClosed
      
       panelSecundario.setVisible(true);
        
    }//GEN-LAST:event_formInternalFrameClosed

    private void btnLimpiarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnLimpiarActionPerformed
       limpiarDatosFarmacia();
    }//GEN-LAST:event_btnLimpiarActionPerformed

    private void btnIngresarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnIngresarActionPerformed
        tabla.setRowCount(0); 
        controlarFarmacia.controlarAccion(evt, obtenerFarmacia());
        System.out.println("Dentre al boton ingresar");
        limpiarDatosFarmacia();
        llenarTabla();
    }//GEN-LAST:event_btnIngresarActionPerformed

    private void btnBuscarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnBuscarActionPerformed
        // TODO add your handling code here:
        llenarTablaConBusqueda(txtBuscar.getText());
        
        
    }//GEN-LAST:event_btnBuscarActionPerformed

    private void btnEliminarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnEliminarActionPerformed
        controlarFarmacia.controlarAccion(evt, obtenerFarmacia()); 
        limpiarDatosFarmacia();
        tabla.setRowCount(0); 
        llenarTabla();
    }//GEN-LAST:event_btnEliminarActionPerformed

    private void tablaDatosFarmaciaMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_tablaDatosFarmaciaMouseClicked
        // TODO add your handling code here:
        
         Farmacia estaFarmacia =new Farmacia();
        if (evt.getClickCount()==2) {
            int fila = tablaDatosFarmacia.rowAtPoint(evt.getPoint());
            
            if(fila > -1){

                spinnerId.setValue((Integer) tablaDatosFarmacia.getValueAt(fila,0));
                txtNitFarmacia.setText(((String) tablaDatosFarmacia.getValueAt(fila,1)));
                txtNombreFarmacia.setText((String) tablaDatosFarmacia.getValueAt(fila,2));
                txtTelefonoFarmacia.setText((String) tablaDatosFarmacia.getValueAt(fila,3));
                txtCorreoFarmacia.setText((String) tablaDatosFarmacia.getValueAt(fila,4));
                txtUbicacionFarmacia.setText((String) tablaDatosFarmacia.getValueAt(fila,5));
                //
                btnModificar.setEnabled(true);
                btnEliminar.setEnabled(true);

                System.out.println("dentre a la funcion llenar la tabla con dos click");
                //                BTNModificar.setVisible(true);
                //                BTNModificar.seetrue);
            }//   17/10/2024 tenemos dos anos para para la practica enviar correo en el momento de entrar a practicas tiene que enviar un correo al sena para pedir instructor de seguimiento. 
            // el id se esta pasando como cero hay que crear un objeto de la clase farmacia y traerlo y asinarselo ahi o mirar como lo hace en la guia
        }
    }//GEN-LAST:event_tablaDatosFarmaciaMouseClicked
    
    
    private void limpiarDatosFarmacia(){
        
        txtNitFarmacia.setText("");
        txtNombreFarmacia.setText("");
        txtTelefonoFarmacia.setText("");
        txtCorreoFarmacia.setText("");
        txtUbicacionFarmacia.setText("");
//        llenarTabla();
        
    }
    
    private void llenarTabla(){
        Farmacia unaFarmacia = new Farmacia();
        tabla = (DefaultTableModel)tablaDatosFarmacia.getModel();
        tabla.setRowCount(0); 
        Iterator<Farmacia> itFarmacia = unaFarmacia.Listar();
        Object[] filaFarmacia = new Object[6];
        
        while (itFarmacia.hasNext()) {
            
            unaFarmacia = itFarmacia.next();
            filaFarmacia[0] = unaFarmacia.getIdFarmacia();
            filaFarmacia[1] = unaFarmacia.getNitFarmacia();
            filaFarmacia[2] = unaFarmacia.getNombreFarmacia();
            filaFarmacia[3] = unaFarmacia.getTelefonoFarmacia();
            filaFarmacia[4] = unaFarmacia.getCorreoFarmacia();
            filaFarmacia[5] = unaFarmacia.getUbicacionFarmacia();
            
            tabla.addRow(filaFarmacia);
          
        }
    }
    
     
    
    private Farmacia obtenerFarmacia (){
        
        Farmacia laFarmacia = new Farmacia();
        
        laFarmacia.setIdFarmacia((Integer)spinnerId.getValue());
        laFarmacia.setNitFarmacia(txtNitFarmacia.getText());
        laFarmacia.setNombreFarmacia(txtNombreFarmacia.getText());
        laFarmacia.setTelefonoFarmacia(txtTelefonoFarmacia.getText());
        laFarmacia.setCorreoFarmacia(txtCorreoFarmacia.getText());
        laFarmacia.setUbicacionFarmacia(txtUbicacionFarmacia.getText());
        
        return (laFarmacia);
    }
    
     private void llenarTablaConBusqueda(String busqueda){
        
        Farmacia unaFarmacia =new Farmacia();
        DefaultTableModel tabla = (DefaultTableModel)tablaDatosFarmacia.getModel();
        Iterator<Farmacia> itFarmacia = unaFarmacia.buscar(busqueda);
        Object[] filaFarmacia = new Object [6];
        
        tabla.setRowCount(0); // es para limpiar la tabla 
        
        while (itFarmacia.hasNext()){
            
            unaFarmacia = itFarmacia.next();
            filaFarmacia[0] = unaFarmacia.getIdFarmacia();
            filaFarmacia[1] = unaFarmacia.getNitFarmacia();
            filaFarmacia[2] = unaFarmacia.getNombreFarmacia();
            filaFarmacia[3] = unaFarmacia.getTelefonoFarmacia();
            filaFarmacia[4] = unaFarmacia.getCorreoFarmacia();
            filaFarmacia[5] = unaFarmacia.getUbicacionFarmacia();
            
            tabla.addRow(filaFarmacia);
        
        }
    }
      
      
      

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnBuscar;
    private javax.swing.JButton btnEliminar;
    private javax.swing.JButton btnIngresar;
    private javax.swing.JButton btnLimpiar;
    private javax.swing.JButton btnModificar;
    private javax.swing.JButton jButton1;
    private javax.swing.JLabel jLabel10;
    private javax.swing.JLabel jLabel11;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JLabel jLabel9;
    private javax.swing.JPopupMenu jPopupMenu1;
    private javax.swing.JRadioButtonMenuItem jRadioButtonMenuItem1;
    private javax.swing.JScrollPane jScrollPane2;
    private javax.swing.JSeparator jSeparator1;
    private javax.swing.JSeparator jSeparator4;
    private javax.swing.JSeparator jSeparator5;
    private javax.swing.JLabel labelFarmacit;
    private javax.swing.JPanel panelFarmacia;
    private javax.swing.JSpinner spinnerId;
    private javax.swing.JTable tablaDatosFarmacia;
    private javax.swing.JTextField txtBuscar;
    private javax.swing.JTextField txtCorreoFarmacia;
    private javax.swing.JTextField txtNitFarmacia;
    private javax.swing.JTextField txtNombreFarmacia;
    private javax.swing.JTextField txtTelefonoFarmacia;
    private javax.swing.JTextField txtUbicacionFarmacia;
    private javax.swing.JLabel vSuperOfertas;
    // End of variables declaration//GEN-END:variables

    
}