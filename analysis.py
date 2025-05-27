def estimate_solar_output(usable_area_m2, panel_efficiency=0.19, irradiance=5.5):
    watts_per_m2 = 1000
    daily_output_kWh = usable_area_m2 * watts_per_m2 * panel_efficiency * irradiance / 1000
    return round(daily_output_kWh * 365, 2)

def estimate_roi(installed_cost, annual_savings):
    payback_period = installed_cost / annual_savings
    return round(payback_period, 2)
