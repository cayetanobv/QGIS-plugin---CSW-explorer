# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CSW_Explorer
 A QGIS plugin
 Retrieving info from a CSW with OWSLib
                             -------------------
        begin                : 2014-08-16
        copyright            : (C) 2014 by Geographica
        email                : cayetano.benavent@geographica.gs
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load CSW_Explorer class from file csw_explorer
    from csw_explorer import CSW_Explorer
    return CSW_Explorer(iface)
