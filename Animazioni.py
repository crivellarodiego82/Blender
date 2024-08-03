import bpy
from mathutils import Quaternion

# Armatura
armature = bpy.data.objects['Umano']

# Passa in modalità Posa
bpy.context.view_layer.objects.active = armature
bpy.ops.object.mode_set(mode='POSE')

# Funzione per applicare la rotazione iniziale, intermedia e finale ad un osso specifico
def set_bone_rotation(bone_name, initial_quat, inter_quat, final_quat, initial_to_inter_delay, inter_to_final_delay, reset_delay):
    bone = armature.pose.bones[bone_name]
    
    # Imposta la rotazione iniziale in quaternione
    bone.rotation_mode = 'QUATERNION'
    bone.rotation_quaternion = initial_quat
    print(f"Rotazione iniziale di {bone_name}: {bone.rotation_quaternion}")
    
    # Funzione per applicare la rotazione intermedia
    def apply_intermediate_rotation():
        bone.rotation_quaternion = inter_quat
        print(f"Rotazione intermedia di {bone_name} applicata: {bone.rotation_quaternion}")
        return None  # Non ripete il timer
    
    # Funzione per applicare la rotazione finale
    def apply_final_rotation():
        bone.rotation_quaternion = final_quat
        print(f"Rotazione finale di {bone_name} applicata: {bone.rotation_quaternion}")
        return None  # Non ripete il timer

    # Funzione per ripristinare la rotazione iniziale (se necessario)
    def reset_initial_rotation():
        bone.rotation_quaternion = initial_quat
        print(f"Rotazione iniziale di {bone_name} ripristinata: {bone.rotation_quaternion}")
        return None  # Non ripete il timer

    # Imposta il ritardo per la rotazione intermedia
    bpy.app.timers.register(apply_intermediate_rotation, first_interval=initial_to_inter_delay)
    
    # Imposta il ritardo per la rotazione finale
    bpy.app.timers.register(apply_final_rotation, first_interval=initial_to_inter_delay + inter_to_final_delay)

    # Ripristinare la rotazione iniziale dopo la finale, imposta un altro timer
    bpy.app.timers.register(reset_initial_rotation, first_interval=initial_to_inter_delay + inter_to_final_delay + reset_delay)

# Definizione delle rotazioni in quaternioni per ossa

# Per 'Omero_Sinistro Su/Giu'
pos_iniziale_sinistra_su_giu = Quaternion((1.000, 0.000, 0.000, 0.000))
Y_r10s_su_giu = Quaternion((0.995, 0.000, 0.000, 0.097))
Y_r90s_su_giu = Quaternion((0.707, 0.000, 0.000, 0.707))

# Per 'Omero_Destro Su/Giu'
pos_iniziale_destra_su_giu = Quaternion((1.000, 0.000, 0.000, 0.000))
Y_r10d_su_giu = Quaternion((0.995, 0.000, 0.000, -0.104))
Y_r90d_su_giu = Quaternion((0.705, 0.000, 0.000, -0.709))

# Per 'Omero_Sinistro Avanti/Indietro'
pos_iniziale_sinistra_avanti_indietro = Quaternion((1.000, 0.000, 0.000, 0.000))
Y_r10s_avanti_indietro = Quaternion((0.988, 0.155, -0.006, 0.000))
Y_r90s_avanti_indietro = Quaternion((0.700, 0.713, -0.027, 0.000))

# Per 'Omero_Destro Avanti/Indietro'
pos_iniziale_destra_avanti_indietro = Quaternion((1.000, 0.000, 0.000, 0.000))
Y_r10d_avanti_indietro = Quaternion((0.988, 0.155, 0.006, 0.000))
Y_r90d_avanti_indietro = Quaternion((0.700, 0.713, 0.027, 0.000))


# Funzione per la sequenza 1: Rotazione dell'Omero Sinistro Su/Giu
def sequenza_1():
    set_bone_rotation('Omero_Sinistro', pos_iniziale_sinistra_su_giu, Y_r10s_su_giu, Y_r90s_su_giu, initial_to_inter_delay=2.0, inter_to_final_delay=2.0, reset_delay=2.0)

# Funzione per la sequenza 2: Rotazione dell'Omero Destro Su/Giu
def sequenza_2():
    set_bone_rotation('Omero_Destro', pos_iniziale_destra_su_giu, Y_r10d_su_giu, Y_r90d_su_giu, initial_to_inter_delay=2.0, inter_to_final_delay=2.0, reset_delay=2.0)

# Funzione per la sequenza 3: Rotazione dell'Omero Sinistro Avanti/Indietro
def sequenza_3():
    set_bone_rotation('Omero_Sinistro', pos_iniziale_sinistra_avanti_indietro, Y_r10s_avanti_indietro, Y_r90s_avanti_indietro, initial_to_inter_delay=2.0, inter_to_final_delay=2.0, reset_delay=2.0)

# Funzione per la sequenza 4: Rotazione dell'Omero Destro Avanti/Indietro
def sequenza_4():
    set_bone_rotation('Omero_Destro', pos_iniziale_destra_avanti_indietro, Y_r10d_avanti_indietro, Y_r90d_avanti_indietro, initial_to_inter_delay=2.0, inter_to_final_delay=2.0, reset_delay=2.0)

# Avvio delle sequenze successive
bpy.app.timers.register(sequenza_1, first_interval=0.0)  # Inizia subito la prima sequenza
bpy.app.timers.register(sequenza_2, first_interval=6.0)  # Avvia la seconda sequenza dopo 6 secondi
bpy.app.timers.register(sequenza_3, first_interval=12.0) # Avvia la terza sequenza dopo 12 secondi
bpy.app.timers.register(sequenza_4, first_interval=18.0) # Avvia la quarta sequenza dopo 18 secondi

print("Script eseguito, in attesa di temporizzatori...")
