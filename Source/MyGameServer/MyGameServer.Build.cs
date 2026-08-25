// Copyright Epic Games, Inc. All Rights Reserved.

using UnrealBuildTool;

public class MyGameServer : ModuleRules
{
	public MyGameServer(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.PCHOrSharedThroughUnity;
		
		PublicDependencyModuleNames.AddRange(new string[] 
		{ 
			"Core",
			"CoreUObject",
			"Engine",
			
			// Server-authoritative GAS
			"GameplayAbilities",
			"GameplayTags",
			"GameplayTasks",
			
			// Online Multiplayer
			"OnlineSubsystem",
			"OnlineSubsystemUtils",
			"Sockets",
			"Networking",
			
			// Data-driven systems
			"Json",
			"JsonUtilities"
		});

		PrivateDependencyModuleNames.AddRange(new string[] 
		{ 
			"MyGame"
		});

		// Server builds exclude UI and editor modules
		PublicDependencyModuleNames.RemoveAll(Module => 
			Module.Contains("Slate") || 
			Module.Contains("Editor") || 
			Module.Contains("PCG")); // PCG is editor/runtime but may not be needed on dedicated server

		bEnableExceptions = false;
		bTreatWarningsAsErrors = true;
		
		PublicDefinitions.Add("WITH_SERVER_CODE=1");
		PublicDefinitions.Add("UE_BUILD_SHIPPING=1");
	}
}
