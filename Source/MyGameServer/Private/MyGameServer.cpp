// Copyright Epic Games, Inc. All Rights Reserved.

#include "MyGameServer.h"
#include "CoreMinimal.h"
#include "Modules/ModuleManager.h"

#define LOCTEXT_NAMESPACE "FMyGameServerModule"

void FMyGameServerModule::StartupModule()
{
	UE_LOG(LogTemp, Log, TEXT("MyGameServer Module: Startup - Dedicated server foundation loaded"));
}

void FMyGameServerModule::ShutdownModule()
{
	UE_LOG(LogTemp, Log, TEXT("MyGameServer Module: Shutdown"));
}

#undef LOCTEXT_NAMESPACE
