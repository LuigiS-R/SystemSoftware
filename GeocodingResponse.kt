package com.example.final_project

data class GeocodingResponse(
    val results: List<Result>,
    val status: String
)

data class Result(
    val geometry: Geometry
)

data class Geometry(
    val location: LocationData
)

data class LocationData(
    val lat: Double,
    val lng: Double
)
