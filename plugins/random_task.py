#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Ivan Vladimir Meza Ruiz 2018
# GPL 3.0

import random

def execute(*args):
    var=args[0]
    msg = random.choice(['Estirarte 5 minutos y hacer 5 minutos de ejercicio.',
                         'Tomar 2 vasos de agua después de despertrte.',
                         'Ver un episodio de tu serie favorita durante la cena.',
                         'Marcarle a un amigo para saber que tal estuvo su día.',
                         'Come un coctel con tu fruta favorita.',
                         'Sonríele a una persona con la que te cruces.',
                         'Ten una cita contigo.',
                         'Planea un picnic con tus personas favoritas.',
                         'Comienza a leer un libro que te llame la atención.',
                         'Péinate diferente.',
                         'Mírate en un espejo di en voz alta "hoy me gusta mi..."',
                         'Ayuda a alguien a sonreir.'])
    return 'set_slot {0} "{1}"'.format(var,msg)
