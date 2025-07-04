package com.example.ifd.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@RestController
@RequestMapping("/api")
public class PredictionController {

    @PostMapping("/predict")
    public ResponseEntity<String> predict(@RequestBody Map<String, Object> payload) {
        // TODO: call Python service for model prediction
        return ResponseEntity.ok("Prediction result placeholder");
    }
}
