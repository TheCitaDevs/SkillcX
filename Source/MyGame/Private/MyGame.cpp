// Copyright Epic Games, Inc. All Rights Reserved.

#include "MyGame.h"
#include "CoreMinimal.h"
#include "Modules/ModuleManager.h"

#define LOCTEXT_NAMESPACE "FMyGameModule"

void FMyGameModule::StartupModule()
{
	// Initialize core systems for server-authoritative multiplayer
	// GAS subsystems are auto-initialized by engine modules
	
	UE_LOG(LogTemp, Log, TEXT("MyGame Module: Startup - Server-authoritative foundation loaded"));
}

void FMyGameModule::ShutdownModule()
{
	// Cleanup handled by engine module system
	
	UE_LOG(LogTemp, Log, TEXT("MyGame Module: Shutdown"));
}

#undef LOCTEXT_NAMESPACE
