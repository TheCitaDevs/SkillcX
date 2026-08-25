// Copyright Epic Games, Inc. All Rights Reserved.

#include "MyGameEditor.h"
#include "CoreMinimal.h"
#include "Modules/ModuleManager.h"

#define LOCTEXT_NAMESPACE "FMyGameEditorModule"

void FMyGameEditorModule::StartupModule()
{
	UE_LOG(LogTemp, Log, TEXT("MyGameEditor Module: Startup"));
}

void FMyGameEditorModule::ShutdownModule()
{
	UE_LOG(LogTemp, Log, TEXT("MyGameEditor Module: Shutdown"));
}

#undef LOCTEXT_NAMESPACE
