#===============================================================================
# EXTRACTION SCRIPT felix_cocktail_calibration.py
#===============================================================================
'''
modifier: mc
eqtime: 30
'''

def main():
    info("Cocktail Machine Calibration")
    # gosub('felix:WaitForMiniboneAccess')
#     gosub('felix:PrepareForAirShot')
#     gosub('common:EvacPipette1')
#     gosub('common:FillPipette1')
#     gosub('felix:PrepareForAirShotExpansion')
#     gosub('common:ExpandPipette1')
#     close(description='Outer Pipette 1')
#     
#===============================================================================
# POST EQUILIBRATION SCRIPT felix_pump_extraction_line.py
#===============================================================================
def main():
    info('Pump after analysis')
    gosub('felix:PumpBone')
    if get_resource_value(name='FelixMiniboneFlag'):
        gosub('felix:PumpMinibone')
#===============================================================================
# POST MEASUREMENT SCRIPT felix_pump_ms.py
#===============================================================================
def main():
	info('Pumping spectrometer')
	open(name='V')
	