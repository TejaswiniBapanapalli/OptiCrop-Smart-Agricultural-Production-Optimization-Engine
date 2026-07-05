erDiagram
    FARMER {
        int FarmerID PK
        string Name
        string Mobile
        string Village
    }

    CROP {
        int CropID PK
        string CropName
        string SoilType
        string Season
        int FarmerID FK
    }

    FERTILIZER {
        int FertilizerID PK
        string FertilizerName
        int CropID FK
    }

    IRRIGATION {
        int IrrigationID PK
        int CropID FK
        string WaterRequirement
        string Schedule
    }

    COST {
        int CostID PK
        int CropID FK
        float SeedCost
        float FertilizerCost
        float LabourCost
        float TotalCost
    }

    FARMER ||--o{ CROP : "cultivates"
    CROP ||--|| FERTILIZER : "has recommendation"
    CROP ||--|| IRRIGATION : "has schedule"
    CROP ||--|| COST : "has estimation"
    }